# Endatabas Demo - 2023-09-11

## Easy Instructions (Manual Mode)

If you came here because you watched the demo, this is probably what you want.

Just copy and paste each command directly from [`commands.ydo`](commands.ydo).
Ignore any lines that begin with a comment (`#`) or keycodes (`@`).
The first `docker pull` command installs `endb` for you, so there are no prerequisites.

Ignore the rest of this README.

## Setup (Automated Mode)

* Requires `ydotool`, which requires root

[Install `ydotool` (1.0.x) from source.](https://askubuntu.com/questions/1413829/how-can-i-install-and-use-the-latest-ydotool-keyboard-automation-tool-working-o)
The `ydotool` available in the 22.04 LTS repo will not work.

## Running (Automated Mode)

1. start 3 terminal tabs in these directories, respectively:
    1. `marketing/2023-09-demo`
    2. `~/tmp/endb`
    3. `~/tmp/endb`
2. start the daemon and run the script in one tab

```sh
systemctl start ydotool
sudo ./loop.py
```

3. switch to the second terminal tab
    * be aware the script will switch to the third tab on its own

All keyboard input other than `<ctrl+c>` and `<alt>` is ignored.
Just tap `<alt>` to run the upcoming command.

## Recording

OBS Studio is recommended.

1. Gnome includes a screencast tool: https://help.gnome.org/users/gnome-help/stable/screen-shot-record.html.en
2. OBS Studio has a flatpak: https://obsproject.com/kb/linux-installation

## Caveat Emptor

Be aware that if you don't get to the end of the commands.ydo "script"
or `<ctrl+c>` the runner, `ydotool` will (quite violently) smash random
keystrokes into whatever window has the focus in GNOME.
It can do some weird things.

## Semi-automated

You can try running this yourself,
but the "script" requires manual intervention at a couple points:

* type out the "SELECT ... AS OF" by hand
  (the script can't know what time is returned from `CURRENT_TIMESTAMP`)
    * this is currently hacked around with some trickery (ctrl+f for `@AS_OF`), so this step isn't required.
* 2x final `<alt>` taps if you want it to clean up after itself.
