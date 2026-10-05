# Nightfox Acrylic for Obsidian

A premium suite of **Acrylic / Frosted Glass** themes for [Obsidian](https://obsidian.md), inspired by the **Zed Editor** and the renowned **Nightfox** palette by [EdenEast](https://github.com/EdenEast/nightfox.nvim).

Currently featuring **Carbonfox Acrylic** — meticulously tuned for maximum legibility, seamless window compositing, and a distraction-free coding & note-taking experience across **Windows 11** and **Linux (GNOME / KDE / Wayland)**.

---

## 🎨 Inspiration & Heritage

- **Color Palette & Aesthetics**: Inspired by the Carbonfox flavor from [Zed Editor](https://zed.dev) and [EdenEast/nightfox.nvim](https://github.com/EdenEast/nightfox.nvim). Features signature high-contrast carbon grays, cyan titles, blue subheadings, and vibrant pink accents.
- **Base Architecture**: Built upon the foundational CSS layout of **[Blur Theme](https://github.com/Jawuj/Blur-Theme) by Jawuj**. Re-engineered from the ground up to eliminate Electron compositor bugs on Linux Wayland, remove visual stacking artifacts, and introduce solid code blocks and floating pill tabs.

---

## ✨ Highlights & Design System

* 🪟 **Floating Island Glass Architecture**:
  * **Central Canvas**: 75% opacity (`rgba(22, 22, 22, 0.75)`) with rounded corners (`14px`), ensuring deep contrast for long reading sessions while softly exposing your desktop wallpaper.
  * **Edges & Sidebars**: 50% opacity (`rgba(22, 22, 22, 0.50)`) for maximum glassiness and wallpaper translucency.
* 💊 **Floating Pill Tabs**:
  * Both editor tabs and sidebar icon tabs feature 360° rounded corners (`border-radius: 8px`). Active tabs float as distinct elevated pills with bright white titles, while inactive tabs remain elegantly dimmed (`50% opacity`).
* 💻 **100% Opaque Code Blocks**:
  * Multiline code blocks sit on solid, opaque `#1a1a1a` cards with subtle borders. No desktop text or wallpaper bleed-through — syntax highlighting in C++, Python, Rust, and LaTeX stays razor-sharp.
  * Inline code (` `code` `) rendered on solid `#202020` pills with Carbonfox Cyan accents.
* 🔲 **High-Contrast 96% Modals**:
  * Settings (`Ctrl+,`), Command Palette (`Ctrl+P`), and Quick Switcher (`Ctrl+O`) are rendered with 96% opacity and a 65% darkened background overlay. Clean, legible, and focused — exactly like the native Zed editor.
* ✔️ **Crisp Vector SVG Checkmarks**:
  * Custom task list checkboxes use inline vector SVG checkmarks that remain pixel-perfect at any DPI scaling (100%, 125%, 150%, 200%).
* 🏷️ **Clean Typography & Accents**:
  * **H1 & Inline Title**: Carbonfox Cyan (`#08bdba`)
  * **H2**: Carbonfox Blue (`#78a9ff`)
  * **H3–H6**: Carbonfox Pink (`#ee5396`)
  * **Italics (`*text*`)**: Pink (`#ee5396`)
  * **UI Icons & Explorer**: Pure White (`#ffffff`) for instant visual navigation.

---

## 🚀 Installation

### Option 1: Manual Installation (Recommended)

1. Open your Obsidian vault folder.
2. Navigate to `.obsidian/themes/` *(create the `themes` directory if it doesn't exist)*.
3. Copy the **`Carbonfox Acrylic`** folder into `.obsidian/themes/`:
   ```
   YourVault/
   └── .obsidian/
       └── themes/
           └── Carbonfox Acrylic/
               ├── manifest.json
               └── theme.css
   ```
4. In Obsidian, open **Settings → Appearance → Themes** and select **Carbonfox Acrylic**.

---

## 🪟 Blur Setup Guide

Because Obsidian is built on Chromium / Electron, true system blur requires hooking into the native OS window compositor:

### 1. Windows 11 (Acrylic Blur)

Windows uses DirectComposition / Desktop Window Manager (DWM) for acrylic effects.

1. In Obsidian, go to **Settings → Community plugins**.
2. Turn off *Restricted mode* and click **Browse**.
3. Search for and install **Translucent BG** (by `@1834925828`).
4. Enable **Translucent BG** and open its settings:
   * **Effect**: Select `Acrylic` (or `BlurBehind` / `Mica` depending on preference).
   * **Opacity**: Adjust the slider to your liking (typically ~`0.7` to `0.85`).
5. *(Optional)* Go to **Settings → Appearance** and toggle **Translucent window** to `ON`.
6. Restart Obsidian to let DWM attach the acrylic surface.

> **Note**: If you experience black borders or sluggish window dragging, ensure **Hardware Acceleration** is turned **ON** in Obsidian (*Settings → Advanced / System*).

---

### 2. Linux GNOME (Blur my Shell)

On GNOME (Wayland or X11), window-level blur is handled natively by GNOME Shell extensions without requiring third-party Electron injectors:

1. Install the **[Blur my Shell](https://github.com/aunetx/blur-my-shell)** extension from [extensions.gnome.org](https://extensions.gnome.org/extension/3193/blur-my-shell/) or via Extension Manager.
2. Open **Blur my Shell Settings**:
   * Navigate to the **Applications** tab.
   * Turn **Blur application windows** to `ON`.
   * Under **Application List / Whitelist**, click **Add** and select **Obsidian** (or enter `md.obsidian.Obsidian` / `obsidian`).
3. *(Recommended Settings)*:
   * **Sigma (Blur radius)**: `30`
   * **Brightness**: `0.85` - `0.90`
4. If running on native Wayland, launch Obsidian with standard Wayland flags:
   ```bash
   obsidian --enable-features=UseOzonePlatform --ozone-platform=wayland
   ```

---

### 3. Other Linux Compositors

- **Hyprland**: Add window rules to `~/.config/hypr/hyprland.conf`:
  ```ini
  windowrulev2 = opacity 0.85 0.85, class:^(obsidian)$
  windowrulev2 = blur, class:^(obsidian)$
  ```
- **KDE Plasma (KWin)**: 
  * Open **System Settings → Window Management → Window Rules**.
  * Add a new rule for `obsidian`:
    * Set **Force Active/Inactive Opacity** to `85%`.
    * Set **Background blur** to `Force: Yes`.

---

## 🗺️ Roadmap

- [x] **Carbonfox Acrylic** (Dark Carbon / Cyan & Pink)
- [ ] **Nightfox Acrylic** (Classic Navy Dark)
- [ ] **Nordfox Acrylic** (Nordic Arctic Dark)
- [ ] **Duskfox Acrylic** (Purple Dusk Dark)
- [ ] **Terafox Acrylic** (Earthy Warm Dark)
- [ ] **Dawnfox Acrylic** (Soft Muted Daylight)
- [ ] **Dayfox Acrylic** (Clean High-Contrast Light)
- [ ] **Style Settings Plugin integration** for customized accent color toggles.

---

## 📜 Credits & License

- Designed and maintained by **[mihail](https://github.com/mihail44b)**.
- Palette colors derived from [EdenEast/nightfox.nvim](https://github.com/EdenEast/nightfox.nvim) and [Zed Editor](https://zed.dev).
- Layout architecture built upon [Jawuj/Blur-Theme](https://github.com/Jawuj/Blur-Theme).
- Released under the [MIT License](LICENSE).
