#!/usr/bin/env python3

import sys
import os
import time
import keyboard
import re

cmd = open("commands.ydo", "r")

def next():
    line = cmd.readline()
    stripped = line.strip()
    if len(line) == 0:
        print("EOF. Quitting.")
        sys.exit(0)
    if len(stripped) > 0 and not re.match('^#.*', stripped):
        return line
    else:
        return next()

while True:
    event = keyboard.read_event()
    if event.event_type == 'down':
        if event.name == 'alt':
            time.sleep(0.2)
            c = next()
            os.system(f"ydotool type --next-delay 5 --key-delay 2 '{c}'")
        elif event.name == 'ctrl' or event.name == 'caps lock':
            print('ctrl detected. press ctrl+c to quit.')
