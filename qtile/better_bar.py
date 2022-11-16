import os

from libqtile import bar, widget
from libqtile.lazy import lazy

from better_widgets import BetterBattery, BetterBluetooth, BetterVolume, BetterPowerline, Discord, Spotify

SCRIPTS_DIR = os.environ["USER_SCRIPTS_DIRECTORY"]


def get_bar(colorscheme: dict, fontsize: int, powerline_size: int):
    """
    Returns the bar.Bar object for the qtile status bar
    """
    bg = colorscheme["bg"]
    fg = colorscheme["fg"]

    # return default_bar
    return bar.Bar([
        widget.TextBox(
            "    ",
            fontsize=fontsize,
            name="Arch Linux icon",
            background=bg,
            foreground=colorscheme["cyan"],),

        BetterPowerline(
            type=0,
            direction="right",
            background=fg,
            foreground=bg,
            fontsize=powerline_size),

        # TODO: Rework group box so that I have numbered workspaces, but also dedicated workspaces like
        #       "IDE", "Discord", "Browser"
        widget.GroupBox(
            visible_groups=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            fontsize=fontsize,
            background=fg,
            foreground=bg,
            margin_x=15,
            # margin_y=,
            padding_x=10,
            padding_y=1,
            borderwidth=2,
            active=bg,
            rounded=True,
            highlight_method="border",
            urgent_alert_method="block",
            urgent_border=colorscheme["red"],
            this_current_screen_border=colorscheme["cyan"],
            # this_screen_border="#F0F0F0",
            # other_current_screen_border="#FFFF00",
            # other_screen_border="#00FFFF",
            disable_drag=True,
            hide_unused=True,
        ),

        BetterPowerline(
            type=0,
            direction="right",
            background=colorscheme["red"],
            foreground=fg,
            fontsize=powerline_size),
        BetterPowerline(
            type=0,
            direction="right",
            background=colorscheme["magenta"],
            foreground=colorscheme["red"],
            fontsize=powerline_size),
        BetterPowerline(
            type=0,
            direction="right",
            background=colorscheme["cyan"],
            foreground=colorscheme["magenta"],
            fontsize=powerline_size),
        BetterPowerline(
            type=0,
            direction="right",
            background=colorscheme["orange"],
            foreground=colorscheme["cyan"],
            fontsize=powerline_size),
        BetterPowerline(
            type=0,
            direction="right",
            background=bg,
            foreground=colorscheme["orange"],
            fontsize=powerline_size),

        widget.Prompt(
            fontsize=fontsize,
            background=bg,
            foreground=fg,
            bell_style=None,
            ignore_dups_history=True,
            prompt=" > ",),

        # Separator between left and right sides
        widget.Spacer(background=bg,),

        Spotify(
            update_interval=5,
            background=bg,
            foreground=colorscheme["green"],
            padding=10),
        Discord(
            update_interval=5,
            background=bg,
            foreground=colorscheme["blue"],
            padding=10),
        widget.TextBox(
            background=bg,
            foreground=bg,
            text=" "),

        BetterPowerline(
            type=0,
            direction="left",
            background=bg,
            foreground=colorscheme["orange"],
            fontsize=powerline_size),
        BetterPowerline(
            type=0,
            direction="left",
            background=colorscheme["orange"],
            foreground=colorscheme["cyan"],
            fontsize=powerline_size),
        BetterPowerline(
            type=0,
            direction="left",
            background=colorscheme["cyan"],
            foreground=colorscheme["magenta"],
            fontsize=powerline_size),
        BetterPowerline(
            type=0,
            direction="left",
            background=colorscheme["magenta"],
            foreground=colorscheme["red"],
            fontsize=powerline_size),
        BetterPowerline(
            type=0,
            direction="left",
            background=colorscheme["red"],
            foreground=fg,
            fontsize=powerline_size),

        BetterVolume(
            fontsize=fontsize,
            update_interval=1,
            background=fg,
            foreground=bg,
            # fontsize=23,
            mouse_callbacks={
                "Button1": lazy.spawn(f"{SCRIPTS_DIR}/audio/mute-all-toggle"),
                "Button3": lazy.group["scratchpad"].dropdown_toggle("mixer"),
            }),

        BetterPowerline(
            type=6,
            direction="left",
            background=fg,
            foreground=bg,
            fontsize=powerline_size),

        widget.Backlight(
            padding=10,
            backlight_name="intel_backlight",
            fontsize=fontsize,
            background=fg,
            foreground=bg,
            format=" {percent:2.0%}"),

        BetterPowerline(
            type=6,
            direction="left",
            background=fg,
            foreground=bg,
            fontsize=powerline_size),

        BetterBattery(
            fontsize=fontsize,
            update_interval=5,
            background=fg,
            foreground=bg,
            low_foreground=colorscheme["red"],
            low_background=fg),

        BetterPowerline(
            type=0,
            direction="left",
            background=fg,
            foreground=bg,
            fontsize=powerline_size),

        BetterBluetooth(
            update_interval=5,
            fontsize=fontsize,
            background=bg,
            foreground=fg,),

        BetterPowerline(
            type=0,
            direction="left",
            background=bg,
            foreground=fg,
            fontsize=powerline_size),

        widget.KeyboardLayout(
            fontsize=fontsize,
            fmt="  {} ",
            configured_keyboards=["us", "ca"],
            mouse_callbacks={
                "Button1": lazy.spawn(f"{SCRIPTS_DIR}/keyboard/toggle-language"),
            },
            background=fg,
            foreground=bg),

        BetterPowerline(
            type=0,
            direction="left",
            background=fg,
            foreground=bg,
            fontsize=powerline_size),

        widget.Clock(
            fontsize=fontsize,
            format="  %b %d ",
            background=bg,
            foreground=fg),
        BetterPowerline(
            type=6,
            direction="left",
            background=bg,
            foreground=fg,
            fontsize=powerline_size),
        widget.Clock(
            fontsize=fontsize,
            format="  %H:%M ",
            background=bg,
            foreground=fg),
        ],
        34, # Bar height
        # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    )


