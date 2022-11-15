# System includes
import os
from subprocess import Popen, PIPE

# Qtile includes
from libqtile.widget import base
from libqtile.lazy import lazy

SCRIPTS_DIR = os.environ['USER_SCRIPTS_DIRECTORY']

class BetterPowerline(base._TextBox):

    defaults = []

    powerline = [
        ("", ""),
        ("", ""),
        ("", ""),
        ("", ""),
        ("", ""),
        ("", ""),
        ("", ""),
        ("", ""),
    ]

    def __init__(self, type, direction, **config):
        super().__init__("", **config)

        # This will take the background, foregound and fontsize arguments
        self.add_defaults(BetterPowerline.defaults)

        # Set the font and the text
        self.font = "Source Code Pro" if direction == "left" else "nerd font icons"
        self.text = BetterPowerline.powerline[type][0 if direction == "right" else 1]

        # Ensure no padding
        self.padding = 0


class BetterVolume(base.ThreadPoolText):

    defaults = []

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(BetterVolume.defaults)

    def _is_muted(self) -> bool:
        """
        Check if the sink is muted
        """
        proc = Popen(f"{SCRIPTS_DIR}/audio/sink-muted", stdout=PIPE)
        out, _ = proc.communicate()
        return True if out.decode("utf-8") == "yes" else False

    def _get_volume_level(self) -> int:
        """
        Get the volume level in percentage
        """
        proc = Popen(f"{SCRIPTS_DIR}/audio/get-volume-level", stdout=PIPE)
        out, _ = proc.communicate()
        return int(out.decode("utf-8").replace('%', ''))

    def poll(self):
        if self._is_muted():
            # Volume is muted, display muted icon
            return " ﱝ"
        vol = self._get_volume_level()
        if 0 <= vol < 33:
            return f" 奄 {vol}% "
        elif vol < 66:
            return f" 奔 {vol}% "
        else:
            return f" 墳 {vol}% "


class BetterBattery(base.ThreadPoolText):

    defaults = []

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(BetterBattery.defaults)
        self.normal_background=config["background"]
        self.normal_foreground=config["foreground"]

    def _get_battery_level(self) -> int:
        """
        Get the battery level in percentage
        """
        proc = Popen(f"{SCRIPTS_DIR}/battery/get-battery-level", stdout=PIPE)
        out, _ = proc.communicate()
        return int(out.decode("utf-8"))

    def _get_charging_state(self) -> int:
        """
        Get the charging state
        """
        proc = Popen(f"{SCRIPTS_DIR}/battery/get-charging-state", stdout=PIPE)
        out, _ = proc.communicate()
        return int(out.decode("utf-8"))

    def _get_icon(self, lvl):
        """
        Get the icon that represents state
         < 5%
        5% <  < 20%
        20% <  < 60%
        60% <  < 85% 
        85% <  < 100% 
         if charging 
        """
        if self._get_charging_state() == 0:
            if lvl <= 10:
                return ""
            elif lvl <= 40:
                return ""
            elif lvl <= 60:
                return ""
            elif lvl <= 85:
                return ""
            else:
                return ""
        else:
            return ""

    def poll(self):
        lvl = self._get_battery_level()
        icon = self._get_icon(lvl)

        if lvl < 40 and self._get_charging_state() == 0:
            self.background=self.low_background
            self.foreground=self.low_foreground
            pass

        return f" {icon} {lvl}% "


class BetterBluetooth(base.ThreadPoolText):

    defaults = []

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(BetterBluetooth.defaults)

    def poll(self):
        proc = Popen(f"{SCRIPTS_DIR}/bluetooth/get-connected-device", stdout=PIPE)
        out, _ = proc.communicate()
        name = out.decode("utf-8")
        if name == "Disabled":
            return "  "
        else:
            return f" {name} "

class Spotify(base.ThreadPoolText):
    defaults = []

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(Spotify.defaults)
        self.mouse_callbacks = {
            "Button1" : lazy.group["spotify"].toscreen(),
        }

    def poll(self):
        proc = Popen([f"{SCRIPTS_DIR}/is-running", "spotify"], stdout=PIPE)
        out, _ = proc.communicate()
        if out is not None:
            s = int(out)
            if s == 1:
                return ""
            else:
                return ""
        else:
            return "ERR"

class Discord(base.ThreadPoolText):
    defaults = []

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(Discord.defaults)
        self.mouse_callbacks = {
            "Button1" : lazy.group["discord"].toscreen(),
        }

    def poll(self):
        proc = Popen([f"{SCRIPTS_DIR}/is-running", "discord"], stdout=PIPE)
        out, _ = proc.communicate()
        if out is not None:
            s = int(out)
            if s == 1:
                return "ﭮ"
            else:
                return ""
        else:
            return "ERR"

