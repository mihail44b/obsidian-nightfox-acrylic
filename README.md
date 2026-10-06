# 🦊 Nightfox Acrylic Theme Pack for Obsidian

A premium collection of minimalist **Acrylic / Frosted Glass** themes for [Obsidian](https://obsidian.md), inspired by the **Zed Editor** and the renowned **Nightfox** palette family created by [EdenEast](https://github.com/EdenEast/nightfox.nvim).

Built on the glass layout foundations of **[Blur Theme](https://github.com/Jawuj/Blur-Theme) by Jawuj**, redesigned and polished for true system translucency, distraction-free note-taking, and cross-platform consistency across **Windows 11** and **Linux (GNOME / KDE / Wayland)**.

<p align="center">
  <img src="assets/win11/carbonfox_win11.gif" width="900" alt="Carbonfox Acrylic Preview" />
</p>

> 📸 Check out the full **[Theme Gallery (GALLERY.md)](GALLERY.md)** for side-by-side previews of all 6 themes on **Windows 11** and **Linux GNOME**.

---

## ✨ Features

- 🪟 **True Frosted Glass Effect** — System-level backdrop translucency across Windows 11 (DirectComposition/DWM) and Linux (Blur my Shell).
- 🎨 **6 Curated Palettes** — 5 immersive dark flavors + 1 tuned daylight theme with vibrant syntax highlights.
- 🖼️ **Custom Wallpaper Support** — Use any custom background image via the Style Settings plugin or a single CSS variable.
- 📑 **Clean Island Geometry** — Floating glass panels with dedicated 8px vertical split gaps for multi-tab workflows.
- 🖋️ **Opaque Code & Reader Blocks** — Syntax-highlighted code blocks and callouts remain crisp and readable without background visual noise.
- 🎛️ **Style Settings Ready** — Easily toggle blur, subtle glow, darkening overlays, and wallpaper directly from Obsidian's UI.

---

## 🎨 Palettes

| Theme | Flavor | Accent Color | Description | Showcase |
| :--- | :---: | :---: | :--- | :---: |
| **Carbonfox Acrylic** | Dark | `#78a9ff` | Carbon grays with vibrant cyan headers & pink accents | [Preview](GALLERY.md#-carbonfox-acrylic) |
| **Duskfox Acrylic** | Dark | `#c4a7e7` | Deep atmospheric purple dusk with soft violet & amber | [Preview](GALLERY.md#-duskfox-acrylic) |
| **Nightfox Acrylic** | Dark | `#719cd6` | The signature deep navy blue with cool white & teal | [Preview](GALLERY.md#-nightfox-acrylic) |
| **Nordfox Acrylic** | Dark | `#81a1c1` | Cool Arctic blues and frost tones inspired by Nord | [Preview](GALLERY.md#-nordfox-acrylic) |
| **Terafox Acrylic** | Dark | `#5a93aa` | Earthy ochres, warm browns, and amber tones | [Preview](GALLERY.md#-terafox-acrylic) |
| **Dawnfox Acrylic** | Light | `#2d81a3` | Soft daylight palette with warm muted pastels | [Preview](GALLERY.md#-dawnfox-acrylic) |

---

## 📦 Installation

1. **Download this repository**:
   - Click the green **Code** button at the top of this GitHub page and select **Download ZIP** (or clone via `git clone https://github.com/mihail44b/obsidian-nightfox-acrylic.git`).
   - Extract the downloaded archive.
2. **Open Obsidian Themes folder**:
   - In Obsidian, go to **Settings → Appearance**.
   - Under **Themes**, click the **folder icon** next to the theme dropdown (this immediately opens your `.obsidian/themes/` folder in your file manager).
3. **Copy theme folder(s)**:
   - Copy the desired theme folder(s) (e.g. `Carbonfox Acrylic` or all 6 folders) into the opened `themes` directory:
     ```text
     .obsidian/themes/
     ├── Carbonfox Acrylic/
     │   ├── manifest.json
     │   └── theme.css
     └── ... (other themes)
     ```
4. **Activate**:
   - Return to Obsidian, open **Settings → Appearance → Themes**, and select your installed theme.

---

## 🖼️ Using with Custom Background Images

For a personalized frosted glass look, you can set any background image or wallpaper behind the glass panels:

### Method 1: via Style Settings Plugin (Recommended, No Code)
1. Install and enable the **Style Settings** community plugin in Obsidian.
2. Open **Settings → Style Settings → Theme Settings**.
3. In **Custom Wallpaper URL**, paste a direct image URL:
   ```text
   url(https://your-image-url.jpg)
   ```

### Method 2: via CSS Snippet
Create a CSS snippet in `.obsidian/snippets/wallpaper.css` with:
```css
body {
    --custom-wallpaper: url("https://your-image-url.jpg"); /* or base64 / local path */
}
```
Enable the snippet in **Settings → Appearance → CSS snippets**.

---

## 🪟 Blur & Translucency Setup Guide

Obsidian is built on Electron / Chromium, so true acrylic and background blur require integration with your operating system's window compositor:

<details>
<summary><b>🪟 Windows 11 (Acrylic Blur via Translucent BG)</b></summary>

Windows utilizes DirectComposition and the Desktop Window Manager (DWM) for acrylic effects:

1. In Obsidian, go to **Settings → Community plugins** (disable *Restricted mode*).
2. Install and enable **Translucent BG** (by `@1834925828`).
3. In **Translucent BG** settings:
   - **Effect**: Select `Acrylic` (or `Mica` / `BlurBehind`).
   - **Opacity**: Adjust between `0.70` - `0.85` based on preference.
4. In **Settings → Appearance**, ensure **Translucent window** is toggled **ON**.
5. Restart Obsidian.

> **Note (Windows 11 Behavior)**: The Acrylic blur effect is dynamically rendered only when the Obsidian window is **focused (active)**. When the window loses focus (e.g., clicking on another app), Windows DWM automatically shifts it to a solid opaque state to optimize system performance. Check out the [Theme Gallery](GALLERY.md) to see this focus transition in action.

> **Tip**: If you notice sluggish dragging or visual glitches, verify that **Hardware Acceleration** is enabled in Obsidian (**Settings → Advanced**).

</details>

<details>
<summary><b>🐧 Linux GNOME (Blur my Shell)</b></summary>

On GNOME (Wayland or X11), native window blur is provided by GNOME Shell extensions:

1. Install the **[Blur my Shell](https://github.com/aunetx/blur-my-shell)** extension via Extension Manager or [extensions.gnome.org](https://extensions.gnome.org/extension/3193/blur-my-shell/).
2. Open **Blur my Shell Settings**:
   - Go to the **Applications** tab.
   - Toggle **Blur application windows** to **ON**.
   - Under **Application List / Whitelist**, click **Add** and select **Obsidian** (or enter `md.obsidian.Obsidian` / `obsidian`).
3. **Recommended Settings**:
   - **Sigma (Blur radius)**: `30`
   - **Brightness**: `0.85` - `0.90`
4. On native Wayland, launch Obsidian with standard Ozone flags:
   ```bash
   obsidian --enable-features=UseOzonePlatform --ozone-platform=wayland
   ```

</details>

<details>
<summary><b>❄️ Other Linux Compositors (Hyprland & KDE Plasma)</b></summary>

- **Hyprland**: Add the following rules to `~/.config/hypr/hyprland.conf`:
  ```ini
  windowrulev2 = opacity 0.85 0.85, class:^(obsidian)$
  windowrulev2 = blur, class:^(obsidian)$
  ```
- **KDE Plasma (KWin)**:
  1. Open **System Settings → Window Management → Window Rules**.
  2. Add a rule for `obsidian`:
     - **Force Active/Inactive Opacity**: `85%`
     - **Background blur**: `Force: Yes`

</details>

---

## 📜 Credits & License

- Created and maintained by **[mihail](https://github.com/mihail44b)**.
- Palette colors derived from [EdenEast/nightfox.nvim](https://github.com/EdenEast/nightfox.nvim) and [Zed Editor](https://zed.dev).
- Glass layout foundation adapted from [Jawuj/Blur-Theme](https://github.com/Jawuj/Blur-Theme).
- Released under the [MIT License](LICENSE).
