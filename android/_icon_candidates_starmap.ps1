# Draw 5 candidate icons for the direct-star-map button.
# Each rendered at 240x240 on a 66-alpha black square background with white
# outline strokes matching the in-game overlay's monochrome style.

Add-Type -AssemblyName System.Drawing

$CellPx     = 300     # each icon cell (with label + button)
$IconPx     = 200     # actual icon "button" size inside a cell
$IconRad    = 60      # glyph radius in each icon
$Stroke     = 18.0     # stroke width for glyph lines
$NumIcons   = 5
$LabelH     = 60
$Padding    = 20

$totalW = $CellPx * $NumIcons + $Padding * 2
$totalH = $CellPx + $LabelH + $Padding * 2

$bmp = New-Object System.Drawing.Bitmap($totalW, $totalH)
$g   = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.Clear([System.Drawing.Color]::FromArgb(255, 40, 40, 50))

$fontHeader = New-Object System.Drawing.Font('Arial', 14, [System.Drawing.FontStyle]::Bold)
$fontLabel  = New-Object System.Drawing.Font('Arial', 16, [System.Drawing.FontStyle]::Bold)
$brushLabel = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
$brushBg    = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(102, 0, 0, 0))  # 66 alpha
$penFrame   = New-Object System.Drawing.Pen(
    [System.Drawing.Color]::FromArgb(102, 255, 255, 255), 4)
$penGlyph   = New-Object System.Drawing.Pen([System.Drawing.Color]::White, $Stroke)
$penGlyph.LineCap = [System.Drawing.Drawing2D.LineCap]::Round
$penGlyph.LineJoin = [System.Drawing.Drawing2D.LineJoin]::Round
$penGlyphThin = New-Object System.Drawing.Pen([System.Drawing.Color]::White, 8.0)
$penGlyphThin.LineCap = [System.Drawing.Drawing2D.LineCap]::Round
$brushGlyph = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)

$labels = @(
    'A · Constellation (current)',
    'B · Folded paper map',
    'C · Location pin',
    'D · Globe / meridians',
    'E · Compass rose'
)

# --------------------------------------------------------------------------
function Draw-IconFrame($cx, $cy) {
    $r = New-Object System.Drawing.RectangleF(
        [float]($cx - $IconPx/2), [float]($cy - $IconPx/2), $IconPx, $IconPx)
    $g.FillRectangle($brushBg, $r)
    $g.DrawRectangle($penFrame,
        [float]($cx - $IconPx/2), [float]($cy - $IconPx/2), $IconPx, $IconPx)
}

# ----- A. Constellation (current) -----
function Draw-Constellation($cx, $cy) {
    Draw-IconFrame $cx $cy
    $r = $IconRad
    $pts = @(
        [System.Drawing.PointF]::new($cx - $r,           $cy + $r * 0.3),
        [System.Drawing.PointF]::new($cx - $r * 0.45,    $cy - $r * 0.5),
        [System.Drawing.PointF]::new([float]$cx,         $cy + $r * 0.1),
        [System.Drawing.PointF]::new($cx + $r * 0.45,    $cy - $r * 0.5),
        [System.Drawing.PointF]::new($cx + $r,           $cy + $r * 0.3)
    )
    for ($i = 0; $i -lt $pts.Length - 1; $i++) {
        $g.DrawLine($penGlyphThin, $pts[$i], $pts[$i + 1])
    }
    foreach ($p in $pts) {
        $dr = 14
        $g.FillEllipse($brushGlyph, $p.X - $dr/2, $p.Y - $dr/2, $dr, $dr)
    }
}

# ----- B. Folded paper map -----
function Draw-FoldedMap($cx, $cy) {
    Draw-IconFrame $cx $cy
    $r = $IconRad
    # Trapezoid folded panels
    # Rough shape: 3 panels, middle wider than sides, slight tilt.
    $y0 = $cy - $r * 0.9
    $y1 = $cy + $r * 0.9
    # Panel 1 (left) tilted right-down
    $panel1 = @(
        [System.Drawing.PointF]::new($cx - $r,        $cy - $r * 0.7),
        [System.Drawing.PointF]::new($cx - $r * 0.4,  $cy - $r * 0.9),
        [System.Drawing.PointF]::new($cx - $r * 0.4,  $cy + $r * 0.7),
        [System.Drawing.PointF]::new($cx - $r,        $cy + $r * 0.9)
    )
    # Panel 2 (mid) tilted opposite
    $panel2 = @(
        [System.Drawing.PointF]::new($cx - $r * 0.4,  $cy - $r * 0.9),
        [System.Drawing.PointF]::new($cx + $r * 0.4,  $cy - $r * 0.7),
        [System.Drawing.PointF]::new($cx + $r * 0.4,  $cy + $r * 0.9),
        [System.Drawing.PointF]::new($cx - $r * 0.4,  $cy + $r * 0.7)
    )
    # Panel 3 (right)
    $panel3 = @(
        [System.Drawing.PointF]::new($cx + $r * 0.4,  $cy - $r * 0.7),
        [System.Drawing.PointF]::new($cx + $r,        $cy - $r * 0.9),
        [System.Drawing.PointF]::new($cx + $r,        $cy + $r * 0.7),
        [System.Drawing.PointF]::new($cx + $r * 0.4,  $cy + $r * 0.9)
    )
    $g.DrawPolygon($penGlyph, $panel1)
    $g.DrawPolygon($penGlyph, $panel2)
    $g.DrawPolygon($penGlyph, $panel3)
    # Small route line across the map
    $g.DrawLine($penGlyphThin,
        [System.Drawing.PointF]::new($cx - $r * 0.7, $cy - $r * 0.2),
        [System.Drawing.PointF]::new($cx + $r * 0.6, $cy + $r * 0.3))
}

# ----- C. Location pin -----
function Draw-LocationPin($cx, $cy) {
    Draw-IconFrame $cx $cy
    $r = $IconRad
    # Teardrop: circle on top + triangle pointing down
    $tipY = $cy + $r * 0.95
    $headCy = $cy - $r * 0.2
    $headR = $r * 0.65
    # Draw teardrop as GraphicsPath
    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $path.AddArc(
        [float]($cx - $headR), [float]($headCy - $headR),
        [float]($headR * 2), [float]($headR * 2),
        225, 270)
    $path.AddLine(
        [float]($cx + $headR * 0.7), [float]($headCy + $headR * 0.7),
        [float]$cx, [float]$tipY)
    $path.AddLine(
        [float]$cx, [float]$tipY,
        [float]($cx - $headR * 0.7), [float]($headCy + $headR * 0.7))
    $path.CloseFigure()
    $g.DrawPath($penGlyph, $path)
    # Center dot
    $dr = $headR * 0.5
    $g.FillEllipse($brushGlyph,
        [float]($cx - $dr/2), [float]($headCy - $dr/2), $dr, $dr)
}

# ----- D. Globe / meridians -----
function Draw-Globe($cx, $cy) {
    Draw-IconFrame $cx $cy
    $r = $IconRad
    # Outer circle
    $g.DrawEllipse($penGlyph,
        [float]($cx - $r), [float]($cy - $r), [float]($r * 2), [float]($r * 2))
    # Horizontal equator
    $g.DrawLine($penGlyphThin,
        [float]($cx - $r), [float]$cy, [float]($cx + $r), [float]$cy)
    # Two latitude arcs
    $latOffsetY = $r * 0.5
    $latRadX = $r * 0.98
    $latRadY = $r * 0.2
    $g.DrawArc($penGlyphThin,
        [float]($cx - $latRadX), [float]($cy - $latOffsetY - $latRadY),
        [float]($latRadX * 2), [float]($latRadY * 2), 0, 180)
    $g.DrawArc($penGlyphThin,
        [float]($cx - $latRadX), [float]($cy + $latOffsetY - $latRadY),
        [float]($latRadX * 2), [float]($latRadY * 2), 180, 180)
    # Vertical meridian (curved)
    $meridianRadX = $r * 0.4
    $meridianRadY = $r
    $g.DrawEllipse($penGlyphThin,
        [float]($cx - $meridianRadX), [float]($cy - $meridianRadY),
        [float]($meridianRadX * 2), [float]($meridianRadY * 2))
}

# ----- E. Compass rose -----
function Draw-Compass($cx, $cy) {
    Draw-IconFrame $cx $cy
    $r = $IconRad
    # Outer ring
    $g.DrawEllipse($penGlyph,
        [float]($cx - $r), [float]($cy - $r), [float]($r * 2), [float]($r * 2))
    # 4-point star (diamond made of two triangles)
    $star = @(
        [System.Drawing.PointF]::new([float]$cx, [float]($cy - $r * 0.85)),
        [System.Drawing.PointF]::new([float]($cx + $r * 0.28), [float]$cy),
        [System.Drawing.PointF]::new([float]$cx, [float]($cy + $r * 0.85)),
        [System.Drawing.PointF]::new([float]($cx - $r * 0.28), [float]$cy)
    )
    $g.FillPolygon($brushGlyph, $star)
    # N marker (small dot above)
    $dr = 10
    $g.FillEllipse($brushGlyph,
        [float]($cx - $dr/2), [float]($cy - $r * 0.85 - $dr - 2), $dr, $dr)
    # Horizontal cross line
    $g.DrawLine($penGlyphThin,
        [float]($cx - $r * 0.85), [float]$cy, [float]($cx + $r * 0.85), [float]$cy)
}

# --------------------------------------------------------------------------
# Header
$headerBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::LightGray)
$g.DrawString('Direct-star-map button — 5 icon candidates',
    $fontHeader, $headerBrush, [float]$Padding, [float]4)

# Draw 5 icons in a row
$drawFuncs = @(
    { Draw-Constellation $args[0] $args[1] },
    { Draw-FoldedMap     $args[0] $args[1] },
    { Draw-LocationPin   $args[0] $args[1] },
    { Draw-Globe         $args[0] $args[1] },
    { Draw-Compass       $args[0] $args[1] }
)
for ($i = 0; $i -lt $NumIcons; $i++) {
    $cx = $Padding + $CellPx * $i + $CellPx / 2
    $cy = $Padding + $CellPx / 2 + 20
    & $drawFuncs[$i] $cx $cy
    # Label
    $labelText = $labels[$i]
    $sizeF = $g.MeasureString($labelText, $fontLabel)
    $lx = $cx - $sizeF.Width / 2
    $ly = $cy + $IconPx / 2 + 10
    $g.DrawString($labelText, $fontLabel, $brushLabel, [float]$lx, [float]$ly)
}

$outPath = 'Q:\Dos_G\StarControl2\Android\_icon_candidates_starmap.png'
$bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose()
$bmp.Dispose()
Write-Host "Wrote $outPath"
