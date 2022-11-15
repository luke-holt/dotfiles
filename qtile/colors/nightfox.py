# from color_utils import scale_brightness

def scale_brightness(color: str, pct: int) -> str:
    """
    Scale the brightness of a color by a percentage value
    """

    # Scale a number x by a percentage s
    scale = lambda x, s: int(round((x * (1 + (s / 100)))))

    r = scale(int(color[1:3], 16), pct)
    g = scale(int(color[3:5], 16), pct)
    b = scale(int(color[5:], 16), pct)

    return f"#{r:02x}{g:02x}{b:02x}"

def blend(color_a: str, color_b: str, factor: float) -> str:
    """
    Blend color_a into color_b by a certain factor (0 < f < 1)
    """

    bl = lambda a, b, f: int(round((a - (a - b) * f)))

    r = bl(int(color_a[1:3], 16), int(color_b[1:3], 16), factor)
    g = bl(int(color_a[3:5], 16), int(color_b[1:3], 16), factor)
    b = bl(int(color_a[5:], 16), int(color_b[1:3], 16), factor)

    return f"#{r:02x}{g:02x}{b:02x}"


carbon_bg = "#161616"
carbon_fg = "#f2f4f8"

carbonfox = {
    "bg"      : carbon_bg,
    "fg"      : carbon_fg,

    "black"   : "#282828",                          # Shade 0.15, -0.15
    "red"     : "#EE5396",                          # Shade 0.15, -0.15
    "green"   : "#25be6a",                          # Shade 0.15, -0.15
    "yellow"  : "#08BDBA",                          # Shade 0.15, -0.15
    "blue"    : "#78A9FF",                          # Shade 0.15, -0.15
    "magenta" : "#BE95FF",                          # Shade 0.15, -0.15
    "cyan"    : "#33B1FF",                          # Shade 0.15, -0.15
    "white"   : "#dfdfe0",                          # Shade 0.15, -0.15
    "orange"  : "#3DDBD9",                          # Shade 0.15, -0.15
    "pink"    : "#FF7EB6",                          # Shade 0.15, -0.15

    "comment" : blend(carbon_fg, carbon_bg, 0.4),   # Blend by 0.4 (Between bg and fg?)

    "bg0"     : scale_brightness(carbon_bg, -4),    # Brighten by -4. Dark bg (status line and float)
    "bg1"     : carbon_bg,                          # Default bg
    "bg2"     : scale_brightness(carbon_bg, 6),     # Brighten by 6. Lighter bg (colorcolm folds)
    "bg3"     : scale_brightness(carbon_bg, 12),    # Brighten by 12. Lighter bg (cursor line)
    "bg4"     : scale_brightness(carbon_bg, 24),    # Brighten by 24. Conceal, border fg

    "fg0"     : scale_brightness(carbon_fg, 6),     # Brighten by 6. Lighter fg
    "fg1"     : carbon_fg,                          # Default fg
    "fg2"     : scale_brightness(carbon_fg, -24),   # Brighten by -24. Darker fg (status line)
    "fg3"     : scale_brightness(carbon_fg, -48),   # Brighten by -48. Darker fg (line numbers, fold colums)

    "sel0"    : "#2a2a2a", # Popup bg, visual selection bg
    "sel1"    : "#525253", # Popup sel bg, search bg
}

if __name__ == "__main__":
    for item in carbonfox:
        print(item)
