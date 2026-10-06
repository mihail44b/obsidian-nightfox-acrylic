import sys
import json
from pathlib import Path
from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parent

# Support either screenshots/ or screenshot/ directory
if (SCRIPT_DIR / "screenshot").exists():
    SCREENSHOTS_DIR = SCRIPT_DIR / "screenshot"
else:
    SCREENSHOTS_DIR = SCRIPT_DIR / "screenshots"

RAW_DIR = SCREENSHOTS_DIR / "raw"
CONFIG_FILE = SCRIPT_DIR / "crop_config.json"

# Calibrated defaults (1844 x 1178 px on 2559 x 1439 display)
DEFAULT_BOX = {
    "left": 395,
    "top": 163,
    "right": 2239,
    "bottom": 1341,
    "width": 1844,
    "height": 1178,
}


def load_config():
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return DEFAULT_BOX.copy()


def save_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)


def calibrate(test_path, ref_path):
    print(f"[*] Calibrating crop area from '{Path(test_path).name}' and '{Path(ref_path).name}'...")
    test = Image.open(test_path).convert("RGB")
    ref = Image.open(ref_path).convert("RGB")

    rw, rh = ref.size
    tw, th = test.size

    cx, cy = rw // 2, rh // 2
    pw, ph = 40, 40
    patch = [ref.getpixel((cx + dx, cy + dy)) for dy in range(ph) for dx in range(pw)]
    sample_points = [(0, 0), (pw - 1, ph - 1), (pw // 2, ph // 2), (pw // 4, ph // 4), (3 * pw // 4, 3 * ph // 4)]

    for y in range(0, th - rh + 1):
        for x in range(0, tw - rw + 1):
            match = True
            for sx, sy in sample_points:
                if test.getpixel((x + cx + sx, y + cy + sy)) != ref.getpixel((cx + sx, cy + sy)):
                    match = False
                    break
            if match:
                full_match = True
                for dy in range(ph):
                    for dx in range(pw):
                        if test.getpixel((x + cx + dx, y + cy + dy)) != patch[dy * pw + dx]:
                            full_match = False
                            break
                    if not full_match:
                        break
                if full_match:
                    cfg = {
                        "left": x,
                        "top": y,
                        "right": x + rw,
                        "bottom": y + rh,
                        "width": rw,
                        "height": rh,
                    }
                    save_config(cfg)
                    print(f"[+] Calibration successful! Crop box: (left={x}, top={y}, right={x+rw}, bottom={y+rh}) -> {rw}x{rh}")
                    return cfg
    print("[-] Could not find exact match between ref and test. Using existing configuration.")
    return load_config()


def crop_image(input_path, output_path, cfg):
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        print(f"[-] File not found: {input_path}")
        return False

    im = Image.open(input_path)
    crop_box = (cfg["left"], cfg["top"], cfg["right"], cfg["bottom"])

    # Gracefully handle slight resolution variations if needed
    if im.width < cfg["right"] or im.height < cfg["bottom"]:
        right = min(im.width, cfg["left"] + cfg["width"])
        bottom = min(im.height, cfg["top"] + cfg["height"])
        crop_box = (cfg["left"], cfg["top"], right, bottom)

    cropped = im.crop(crop_box)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(output_path)
    print(f"[+] Cropped: {input_path.name} -> {output_path.name} ({cropped.size[0]}x{cropped.size[1]})")
    return True


def main():
    cfg = load_config()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    args = sys.argv[1:]

    # Calibration mode
    if "--calibrate" in args:
        ref_candidates = [
            SCREENSHOTS_DIR / "ref.png",
            RAW_DIR / "ref.png",
        ]
        test_candidates = [
            RAW_DIR / "test_raw.png",
            SCREENSHOTS_DIR / "test.png",
            RAW_DIR / "test.png",
        ]
        ref_path = next((p for p in ref_candidates if p.exists()), None)
        test_path = next((p for p in test_candidates if p.exists()), None)

        if ref_path and test_path:
            cfg = calibrate(test_path, ref_path)
        else:
            print("[-] Could not find ref.png and test/test_raw.png for calibration.")
        return

    # Specific file passed via CLI
    if args:
        inp = Path(args[0])
        if not inp.exists() and (RAW_DIR / inp).exists():
            inp = RAW_DIR / inp
        elif not inp.exists() and (SCREENSHOTS_DIR / inp).exists():
            inp = SCREENSHOTS_DIR / inp

        if len(args) > 1:
            out = Path(args[1])
            if not out.is_absolute():
                out = SCREENSHOTS_DIR / out
        else:
            # Strip _raw if present
            stem = inp.stem
            if stem.lower().endswith("_raw"):
                stem = stem[:-4]
            out = SCREENSHOTS_DIR / f"{stem}{inp.suffix}"

        crop_image(inp, out, cfg)
        return

    # Default: Batch mode over RAW_DIR
    print("=" * 60)
    print(" Obsidian Screenshot Cropper")
    print(f" Source: {RAW_DIR}")
    print(f" Output: {SCREENSHOTS_DIR}")
    print(f" Target Box: left={cfg['left']}, top={cfg['top']}, right={cfg['right']}, bottom={cfg['bottom']} ({cfg['width']}x{cfg['height']} px)")
    print("=" * 60)

    # Scan for files ending with _raw
    all_files = list(RAW_DIR.glob("*.*"))
    raw_files = [
        f for f in all_files
        if f.is_file()
        and f.suffix.lower() in [".png", ".jpg", ".jpeg"]
        and f.stem.lower().endswith("_raw")
    ]

    if not raw_files:
        print(f"[*] No '*_raw.png' files found in '{RAW_DIR.name}/'.")
        print("    Usage workflow:")
        print(f"    1. Put your full desktop screenshot into '{SCREENSHOTS_DIR.name}/raw/<name>_raw.png'")
        print(f"       (e.g., 'carbonfox_raw.png', 'duskfox_raw.png')")
        print("    2. Run: python crop.py")
        print(f"    3. Cropped images will be placed in '{SCREENSHOTS_DIR.name}/<name>.png'")
        return

    print(f"[*] Found {len(raw_files)} raw screenshot(s):")
    for f in raw_files:
        target_stem = f.stem[:-4]  # Remove '_raw'
        out_path = SCREENSHOTS_DIR / f"{target_stem}{f.suffix}"
        crop_image(f, out_path, cfg)

    print(f"\n[OK] All cropped screenshots saved to: {SCREENSHOTS_DIR}")


if __name__ == "__main__":
    main()
