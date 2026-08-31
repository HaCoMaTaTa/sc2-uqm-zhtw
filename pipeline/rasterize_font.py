r"""
UQM font rasterizer: convert a TTF/OTF Chinese font into UQM .fon/ directory
format (per-character PNG + kerndat.fnt).

Usage:
  python rasterize_font.py \
      --ref-font  Q:\Dos_G\StarControl2\uqm-work\extracted\base\base\fonts\slab.fon \
      --ttf       C:\Windows\Fonts\NotoSansTC-VF.ttf \
      --chars     "測試繁體中文你好世界" \
      --out       Q:\Dos_G\StarControl2\uqm-work\zh-TW-addon\content\base\fonts\slab.fon

Behaviour:
  1. Copies the reference font's kerndat.fnt to the output (keeps original
     Latin metadata & kerning).
  2. Copies every reference PNG that's not in the CJK range (keeps original
     Latin glyphs intact).
  3. Rasterizes each --chars codepoint from the CJK TTF, cropping to visible
     bounds, height matches reference cell_height.
  4. Emits PNGs as PIL mode 'L' (grayscale with anti-aliasing).
"""

import argparse
import shutil
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def parse_kerndat(kerndat_path: Path):
    """Parse header line: '<name>.fon <cell_h> <?> <?> <baseline>'.

    Some HD fonts (e.g. mm-hd/fonts/pkunk.fon has just 'pkunk.fon 44') ship a
    truncated header. Pad with zeros so parsing doesn't crash.
    """
    lines = kerndat_path.read_text(encoding="ascii", errors="ignore").splitlines()
    header = lines[0].split()
    while len(header) < 5:
        header.append("0")
    return {
        "name":       header[0],
        "cell_h":     int(header[1]),
        "unknown1":   int(header[2]),
        "unknown2":   int(header[3]),
        "baseline":   int(header[4]),
        "kern_lines": lines[1:],
    }


def rasterize_char(ttf: ImageFont.FreeTypeFont, char: str, png_height: int,
                   latin_top: int, latin_bottom: int,
                   cjk_em_top: int, cjk_em_bot: int):
    """Render a single CJK char to a mode='L' PIL Image, preserving the
    character's natural vertical position within the CJK em-box.

    Args:
      png_height:    total PNG height (matches other glyphs in the font)
      latin_top:     first visible pixel row of the reference 'A'
      latin_bottom:  last visible pixel row of the reference 'A' (inclusive)
      cjk_em_top:    row of CJK em-box top in scratch canvas
      cjk_em_bot:    row of CJK em-box bottom in scratch canvas (exclusive)

    Vertical layout: crops the scratch to CJK em rows (NOT tight bbox), so
    chars like `一` (thin horizontal in middle), `─` (box-drawing horizontal),
    `…` (dots at bottom) retain their natural in-em position. The em-box is
    then centered on Latin baseline in the final PNG.
    """
    # 1) Draw into a scratch canvas at a known pen position
    scratch_size = png_height * 6
    pen_x = png_height
    pen_y = png_height * 2  # baseline near middle of scratch
    scratch = Image.new("L", (scratch_size, scratch_size), color=0)
    ImageDraw.Draw(scratch).text((pen_x, pen_y), char, fill=255, font=ttf,
                                  anchor="ls")
    ink_bbox = scratch.getbbox()
    if ink_bbox is None:
        return Image.new("L", (1, png_height), color=0)
    ink_left, _, ink_right, _ = ink_bbox

    # 2) Crop to CJK em-box (fixed vertical range, tight horizontal width)
    #    - Width: tight around ink for kerning
    #    - Height: full em-box so per-char in-em vertical position is preserved
    em_slice = scratch.crop((ink_left, cjk_em_top, ink_right, cjk_em_bot))
    em_h = em_slice.height

    # 3) Map em-box to final PNG.
    #    Align CJK baseline (em_bot) with latin_bottom + 1 (one pixel below
    #    Latin baseline; CJK glyphs typically descend slightly).
    canvas_w = max(em_slice.width + 2, 1)
    final = Image.new("L", (canvas_w, png_height), color=0)
    target_baseline = latin_bottom + 1
    y_offset = target_baseline - em_h  # em top row in final
    # Clamp so we don't overflow the PNG boundaries
    if y_offset < 0:
        # em is taller than baseline allows; crop from em top
        crop_amount = -y_offset
        em_slice = em_slice.crop((0, crop_amount, em_slice.width, em_h))
        y_offset = 0
    if y_offset + em_slice.height > png_height:
        # em bottom would overflow; crop from em bottom
        keep = png_height - y_offset
        em_slice = em_slice.crop((0, 0, em_slice.width, keep))
    final.paste(em_slice, (1, y_offset))
    return final


def measure_cjk_em(ttf: ImageFont.FreeTypeFont, png_height: int):
    """Measure the CJK em-box in scratch-canvas coordinates by rendering a
    known full-body CJK char. Returns (em_top, em_bot) in scratch rows.

    Falls back to `getmetrics()` if the sample char can't be rendered.
    """
    scratch_size = png_height * 6
    pen_x = png_height
    pen_y = png_height * 2  # matches rasterize_char()

    # Try full-body CJK reference chars in order of preference
    for sample in "國中王目日":
        scratch = Image.new("L", (scratch_size, scratch_size), color=0)
        ImageDraw.Draw(scratch).text((pen_x, pen_y), sample, fill=255,
                                      font=ttf, anchor="ls")
        bbox = scratch.getbbox()
        if bbox is not None:
            _, ink_top, _, ink_bot = bbox
            # Extend slightly below ink_bot for CJK punct descenders (like 。)
            # and slightly above ink_top for over-baseline strokes.
            em_top = ink_top - 1
            em_bot = ink_bot + 1
            return max(0, em_top), min(scratch_size, em_bot)

    # Fallback: font metrics (ascent above baseline, descent below)
    ascent, descent = ttf.getmetrics()
    em_top = pen_y - ascent
    em_bot = pen_y + descent
    return max(0, em_top), min(scratch_size, em_bot)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref-font", required=True, type=Path,
                    help="Reference UQM .fon/ directory (kerndat.fnt + PNGs)")
    ap.add_argument("--ttf", required=True, type=Path,
                    help="Path to Chinese TTF/OTF (e.g., NotoSansTC-VF.ttf)")
    ap.add_argument("--chars", default="",
                    help="String of characters to rasterize (may include CJK)")
    ap.add_argument("--chars-file", type=Path, default=None,
                    help="Read additional characters from this UTF-8 file (union with --chars)")
    ap.add_argument("--out", required=True, type=Path,
                    help="Output .fon/ directory")
    ap.add_argument("--font-size", type=int, default=None,
                    help="TTF pixel size (default: reference cell_height)")
    ap.add_argument("--weight", type=int, default=700,
                    help="Font weight (wght axis) for variable fonts. Default: 700 (Bold). "
                         "Common values: 300 Light, 400 Regular, 500 Medium, 700 Bold, "
                         "800 ExtraBold, 900 Black.")
    ap.add_argument("--extra-padding", type=int, default=1,
                    help="Extra horizontal padding around glyph")
    ap.add_argument("--no-aa", action="store_true",
                    help="Disable antialiasing: threshold output to pure black/white. "
                         "For pixel bitmap fonts (Ark Pixel, Fusion Pixel, etc.).")
    ap.add_argument("--aa-threshold", type=int, default=64,
                    help="Threshold value for --no-aa (0-255, default: 64)")
    ap.add_argument("--png-height", type=int, default=None,
                    help="Override output PNG height (default: use reference PNG height). "
                         "For pixel fonts at design sizes different from reference height.")
    ap.add_argument("--latin-top", type=int, default=None,
                    help="Override latin_top (row where Latin 'A' ink starts). "
                         "Useful with --png-height to control CJK vertical placement.")
    ap.add_argument("--latin-bottom", type=int, default=None,
                    help="Override latin_bottom (row where Latin 'A' baseline sits). "
                         "Set smaller than default to create empty space below CJK ink "
                         "(reduces menu-item overlap without recompiling engine).")
    ap.add_argument("--cjk-scale", type=float, default=1.0,
                    help="Scale CJK ink size relative to Latin cap height (0.5-1.0). "
                         "Default 1.0 = CJK matches Latin. Use <1.0 for cramped UI "
                         "fonts (label/micro/tiny) where CJK would otherwise get "
                         "bottom-clipped by tight text-boxes. Latin PNGs unchanged.")
    ap.add_argument("--vertalign-adjust", type=int, default=0,
                    help="Bump kerndat VertAlign by this many rows. "
                         "Positive N shifts every rendered glyph DOWN by N pixels "
                         "on-screen (HotSpot.y = png_h - VertAlign shrinks by N). "
                         "Useful when a dialog frame has top-clipping issues: "
                         "moving the baseline down gives CJK ascender chars "
                         "(我/普/族/首/高) breathing room at the top. "
                         "Bottom of dialog frame must have enough headroom for the "
                         "shifted descender. PNGs unchanged.")
    args = ap.parse_args()

    if not args.ref_font.is_dir():
        raise SystemExit(f"Reference font dir not found: {args.ref_font}")
    kerndat_src = args.ref_font / "kerndat.fnt"
    if not kerndat_src.exists():
        raise SystemExit(f"Missing kerndat.fnt in {args.ref_font}")

    meta = parse_kerndat(kerndat_src)
    cell_h   = meta["cell_h"]
    baseline_hint = meta["baseline"]  # kept for reference/debug, not used directly

    # Detect actual PNG height and Latin-cap-height range from reference 'A'.
    sample_png = args.ref_font / "00041.png"
    if not sample_png.exists():
        pngs = sorted(args.ref_font.glob("*.png"))
        if not pngs:
            raise SystemExit(f"No PNG glyphs in {args.ref_font}")
        sample_png = pngs[0]
    ref_a = Image.open(sample_png).convert("L")
    png_height = ref_a.size[1]
    ref_bbox = ref_a.getbbox()
    if ref_bbox is None:
        raise SystemExit(f"Reference glyph {sample_png} appears blank")
    _, latin_top, _, latin_bottom = ref_bbox

    # Track original ref PNG height so we know whether to upscale Latin PNGs.
    orig_png_height = png_height
    upscale_ratio = 1.0

    # Optional override: for pixel fonts at design height != reference height.
    # Scale latin_top/latin_bottom proportionally so CJK baseline stays sensible.
    if args.png_height is not None and args.png_height != png_height:
        scale = args.png_height / png_height
        latin_top = int(round(latin_top * scale))
        latin_bottom = int(round(latin_bottom * scale))
        png_height = args.png_height
        upscale_ratio = scale  # Latin PNGs and kerndat will be scaled by this.
        print(f"PNG height OVERRIDDEN to {png_height} (scaled latin_top={latin_top}, latin_bottom={latin_bottom}, latin PNGs will bicubic-scale x{upscale_ratio:.3f})")
    # Explicit latin_top/bottom overrides (WINS over scaling). Use this to
    # produce PNGs where CJK ink sits high (top-aligned) with empty rows
    # below. Since UQM's HotSpot.y = png_height - VertAlign (PNG bottom =
    # baseline), empty bottom rows don't shift ink but expand PNG upward,
    # which combined with pushing latin_bottom UP creates a "descender gap"
    # between adjacent menu items → reduces visual overlap.
    if args.latin_top is not None:
        latin_top = args.latin_top
        print(f"latin_top OVERRIDDEN to {latin_top}")
    if args.latin_bottom is not None:
        latin_bottom = args.latin_bottom
        print(f"latin_bottom OVERRIDDEN to {latin_bottom}")

    latin_cap_h = latin_bottom - latin_top
    bottom_pad_rows = 0  # deprecated headroom variable; kept for backwards code paths (no effect)

    print(f"Reference:  {meta['name']}  png_h={png_height}  latin_top={latin_top}  latin_bottom={latin_bottom}  cap_h={latin_cap_h}  (kerndat baseline={baseline_hint})")
    print(f"TTF:        {args.ttf}")

    # Use font size slightly larger than Latin cap height so CJK visually
    # matches Latin (Chinese chars are typically less top-heavy than Latin caps).
    # --cjk-scale < 1.0 shrinks CJK ink so it fits within cramped UI text-boxes
    # (avoids bottom-clipping in outfit stats, planet-info panels, etc).
    base_font_size = args.font_size or max(6, latin_cap_h + 2)
    if args.cjk_scale != 1.0 and 0.5 <= args.cjk_scale <= 1.0:
        font_size = max(6, int(round(base_font_size * args.cjk_scale)))
        print(f"CJK scale {args.cjk_scale:.2f}: font_size {base_font_size} -> {font_size}")
    else:
        font_size = base_font_size
    ttf = ImageFont.truetype(str(args.ttf), font_size)

    # Try to set weight axis for Variable Fonts (Noto Sans TC VF, Source Han Sans VF)
    try:
        ttf.set_variation_by_axes([args.weight])
        print(f"Weight axis set to: {args.weight}")
    except (OSError, AttributeError) as e:
        # Non-variable font or unsupported axis; fall back to default weight
        print(f"Weight axis not applied ({e}); using font's default weight.")

    # Prepare output dir
    args.out.mkdir(parents=True, exist_ok=True)

    # Copy or scale kerndat.fnt.
    # When --png-height differs from ref, we upscale Latin PNGs (bicubic below)
    # and correspondingly scale kerndat's cell_h and per-glyph advance values,
    # so the engine's line-height and glyph-width metrics stay consistent.
    # When --cjk-headroom > 0, we ALSO bump cell_h + VertAlign by K rows so
    # engine's HotSpot.y = png_h - VertAlign stays the same → baseline visual
    # position unchanged, PNG's extra bottom rows sit below baseline as
    # descender pad (which UI text-boxes clip harmlessly instead of ink).
    kerndat_lines = kerndat_src.read_text(encoding="ascii", errors="ignore").splitlines()
    if kerndat_lines:
        header = kerndat_lines[0].split()
        while len(header) < 5:
            header.append("0")
        _adv_re = re.compile(r"^([0-9a-fA-F]+)\s+(-?\d+)\s+(-?\d+)\s*$")

        if upscale_ratio != 1.0:
            for idx in range(1, 5):
                try:
                    header[idx] = str(int(round(int(header[idx]) * upscale_ratio)))
                except (ValueError, IndexError):
                    pass
            for i in range(1, len(kerndat_lines)):
                m = _adv_re.match(kerndat_lines[i])
                if m:
                    hexc = m.group(1)
                    adv_x = int(round(int(m.group(2)) * upscale_ratio))
                    adv_y = int(round(int(m.group(3)) * upscale_ratio))
                    kerndat_lines[i] = f"{hexc} {adv_x} {adv_y}"
            print(f"kerndat scaled x{upscale_ratio:.3f}")

        if bottom_pad_rows > 0:
            # Bump ONLY VertAlign (index 4) by K rows. Leaves cell_h (line
            # height) unchanged so text density in cramped UI (like outfit
            # stats panel) is preserved. VertAlign+K keeps HotSpot.y stable:
            #   HotSpot.y = new_H - new_VA = (H_old+K) - (VA_old+K) = old
            # → baseline visual position unchanged. Extra K PNG rows sit
            # BELOW the line box as an overshoot pad; UI clip hits blank space.
            try:
                header[4] = str(int(header[4]) + bottom_pad_rows)
            except (ValueError, IndexError):
                pass
            print(f"kerndat VertAlign+{bottom_pad_rows} (descender pad, cell_h unchanged)")

        if args.vertalign_adjust != 0:
            # Bump VertAlign by N (unlike bottom_pad_rows, PNG size unchanged).
            # HotSpot.y = png_h - VertAlign shrinks by N → glyphs draw N pixels
            # lower on-screen. Fixes top-clipping when dialog frame is tight.
            try:
                old_va = int(header[4])
                header[4] = str(old_va + args.vertalign_adjust)
                print(f"kerndat VertAlign {old_va} -> {header[4]} (glyphs draw {args.vertalign_adjust} rows lower)")
            except (ValueError, IndexError):
                pass

        kerndat_lines[0] = " ".join(header)

    (args.out / "kerndat.fnt").write_text("\n".join(kerndat_lines) + "\n", encoding="ascii")

    # Copy (and optionally bicubic-upscale) reference PNGs.
    # Upscale keeps the ORIGINAL font's Latin style; only the pixel dimensions
    # grow, so Latin visual identity is preserved but size matches CJK target.
    # If bottom_pad_rows > 0, each Latin PNG gets K blank rows added at bottom
    # to expand its canvas, matching the new png_height for CJK glyphs.
    n_copied = 0
    n_scaled = 0
    for png in args.ref_font.glob("*.png"):
        img = Image.open(png)
        if upscale_ratio != 1.0:
            new_w = max(1, int(round(img.width * upscale_ratio)))
            new_h = max(1, int(round(img.height * upscale_ratio)))
            img = img.resize((new_w, new_h), Image.Resampling.BICUBIC)
            n_scaled += 1
        if bottom_pad_rows > 0:
            # Pad K blank rows at bottom (Latin ink unchanged, extra empty
            # space at bottom for CJK descender clearance).
            padded = Image.new(img.mode, (img.width, img.height + bottom_pad_rows), 0)
            padded.paste(img, (0, 0))
            img = padded
        img.save(args.out / png.name, "PNG")
        n_copied += 1
    scale_note = f" ({n_scaled} bicubic-scaled x{upscale_ratio:.3f})" if upscale_ratio != 1.0 else ""
    pad_note = f" + {bottom_pad_rows} bottom pad rows" if bottom_pad_rows > 0 else ""
    print(f"Copied {n_copied} reference PNGs{scale_note}{pad_note}, Latin style preserved")

    # Measure the CJK em-box once so all glyphs share the same reference frame
    cjk_em_top, cjk_em_bot = measure_cjk_em(ttf, png_height)
    print(f"CJK em-box: rows [{cjk_em_top}, {cjk_em_bot}] (height {cjk_em_bot - cjk_em_top}px)")

    # Rasterize CJK chars from --chars (deduped, union with --chars-file)
    all_chars = args.chars
    if args.chars_file and args.chars_file.exists():
        all_chars += args.chars_file.read_text(encoding="utf-8")
    unique = sorted(set(all_chars) - {"\r", "\n", "\t", " "})
    n_new = 0
    n_skip = 0
    n_over = 0
    for ch in unique:
        cp = ord(ch)
        if cp < 0x80:  # skip ASCII - Latin is already there
            n_skip += 1
            continue
        try:
            img = rasterize_char(ttf, ch, png_height, latin_top, latin_bottom,
                                 cjk_em_top, cjk_em_bot)
        except Exception as e:
            print(f"  ! failed U+{cp:04X} '{ch}': {e}")
            continue
        # Pad horizontally for CJK legibility
        if args.extra_padding > 0:
            padded = Image.new("L", (img.width + args.extra_padding * 2, img.height), 0)
            padded.paste(img, (args.extra_padding, 0))
            img = padded
        # Threshold to pure B/W for pixel fonts
        if args.no_aa:
            img = img.point(lambda p: 255 if p > args.aa_threshold else 0)
        out_path = args.out / f"{cp:05x}.png"
        overwrite = out_path.exists()
        img.save(out_path, "PNG", optimize=True)
        if overwrite:
            n_over += 1
        else:
            n_new += 1

    print(f"Rasterized: {n_new} new PNGs, {n_over} overwrites, {n_skip} ASCII skipped")
    print(f"Total unique input chars: {len(unique)}")
    print(f"Output: {args.out}")


if __name__ == "__main__":
    main()
