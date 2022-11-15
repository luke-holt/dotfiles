

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

if __name__ == "__main__":
    for i in range(10):
        print(scale_brightness("#FFFFFF", -(i + 1) * 10))
