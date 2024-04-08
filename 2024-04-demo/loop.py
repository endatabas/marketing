#!/usr/bin/env python3

import sys
import os
import time
import keyboard
import re
from time import gmtime, strftime

cmd = open("commands.ydo", "r")
saved_timestamp = None

def reset():
    os.system('./reset.sh')

def escape(s):
    return re.sub(r'"', '\\"', s)

# HACK: this is awful, but it beats typing by hand and slowing the demo
def save_current_timestamp(c):
    global saved_timestamp
    if re.match('.*CURRENT_TIMESTAMP.*', c):
        saved_timestamp = strftime("%Y-%m-%dT%H:%M:%S", gmtime())

def test_current_timestamp():
    if saved_timestamp is None:
        print('Error: CURRENT_TIMESTAMP was never saved.')
        exit(1)

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
    elif re.match('^@RETURN$', c.strip()):
        # 28 = RETURN
        os.system('ydotool key --key-delay 1 28:1 28:0')
    elif re.match('^@AS_OF$', c.strip()):
        test_current_timestamp()
        os.system(f'ydotool type --next-delay 2 --key-delay 0 "SELECT * FROM products FOR SYSTEM_TIME AS OF {saved_timestamp};"')
        os.system('ydotool key --key-delay 1 28:1 28:0')
    else:
        os.system(f'ydotool type --next-delay 2 --key-delay 0 "{c}"')
        save_current_timestamp(c)

print('resetting environment. ignore any docker volume errors.')
reset()
print('event loop starting. press <alt> to begin. ctrl+c to quit.')
while True:
    event = keyboard.read_event()
    if event.event_type == 'down':
        if event.name == 'alt':
            run_next()
        elif event.name == 'ctrl' or event.name == 'caps lock':
            print('ctrl detected. press ctrl+c to quit.')
