import sys
import subprocess


from .base import AudioBridge
from ...utils import shellify as _


class USBAudioBridge(AudioBridge):
    name = "usbaudio"

    def run(self, device_id=None):
        if device_id is None:
            command = "{usbaudio}"
        else:
            command = "{usbaudio} --serial {device_id}"
        subprocess.Popen(
            _(command.format(
                usbaudio=self.get_path(),
                device_id=device_id
            )),
            stdout=sys.stdout,
            stderr=sys.stderr
        )
