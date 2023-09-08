# Endatabas Demo - 2023-09-11

## Running

Requires `ydotool`, which requires root.
[Install `ydotool` (1.0.x) from source.](https://askubuntu.com/questions/1413829/how-can-i-install-and-use-the-latest-ydotool-keyboard-automation-tool-working-o)
The `ydotool` available in the 22.04 LTS repo will not work.

Start the daemon, run the script, then switch to a fresh terminal window/tab:

```sh
systemctl start ydotool
sudo ./loop.py
```

All keyboard input other than `<ctrl+c>` and `<alt>` is ignored.
Just tap `<alt>` to run the upcoming command.

NOTE: Be aware that if you don't get to the end of the commands.ydo "script"
or `<ctrl+c>` the runner, `ydotool` will (quite violently) smash random
keystrokes into whatever window has the focus in GNOME.
It can do some weird things.

## Semi-automated

You can try running this yourself,
but the "script" requires manual intervention at a couple points:

* type out the "SELECT ... AS OF" by hand
  (the script can't know what time is returned from `CURRENT_TIMESTAMP`)
* 2x final `<alt>` taps if you want it to clean up after itself.
