import nightfox

color_schemes = {
    "carbonfox": nightfox.carbonfox,
}

def ColorScheme(scheme: str) -> dict:
    return color_schemes[scheme]

