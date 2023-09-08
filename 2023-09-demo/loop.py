#!/usr/bin/env python3

import sys
import os
import time
import keyboard
import re

cmd = open("commands.ydo", "r")

def reset():
    os.system('./reset.sh')

def escape(s):
    return re.sub(r'"', '\\"', s)

def get_next():
    line = cmd.readline()
    stripped = line.strip()
    if len(line) == 0:
        print("EOF. Quitting.")
        sys.exit(0)
    if len(stripped) > 0 and not re.match('^#.*', stripped):
        return line
    else:
        return get_next()

def run_next():
    time.sleep(0.2) # needed to avoid seeing ALT in keydown state
    c = escape(get_next())
    if re.match('^@CTRL\+L$', c.strip()):
        # 29 = CTRL, 38 = 'L'
        os.system('ydotool key --key-delay 1 29:1 38:1 38:0 29:0')
    elif re.match('^@CTRL\+D$', c.strip()):
        # 29 = CTRL, 32 = 'D'
        os.system('ydotool key --key-delay 1 29:1 32:1 32:0 29:0')
    elif re.match('^@CTRL\+PGDN$', c.strip()):
        # 29 = CTRL, 109 = 'PGDN'
        os.system('ydotool key --key-delay 1 29:1 109:1 109:0 29:0')
    else:
        os.system(f'ydotool type --next-delay 2 --key-delay 0 "{c}"')

print('resetting environment. ignore any docker volume errors.')
reset()
print('event loop starting. switch to a new tab/window and press <alt> to begin.')
while True:
    event = keyboard.read_event()
    if event.event_type == 'down':
        if event.name == 'alt':
            run_next()
        elif event.name == 'ctrl' or event.name == 'caps lock':
            print('ctrl detected. press ctrl+c to quit.')
