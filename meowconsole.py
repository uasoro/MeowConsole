#!/usr/bin/env python3
import os
import sys
import time
import random

cat_faces = [
    r"""
 /\_/\
( o.o )
 > ^ <
""",
    r"""
 /\_/\
( ^.^ )
 > ^ <
""",
    r"""
 /\_/\
( -.- )
 > ^ <
""",
    r"""
 /\_/\
( >.< )
 > ^ <
"""
]

messages = [
    "Hello, human!",
    "How are you?",
    "I'm a happy cat!",
    "Meow!",
    "Purr...",
    "Meow! What's up?",
    "I saw a red dot!",
    "Stroke me...mentally",
    "I'm a good kitty, honestly!",
    "need to get some sleep...",
    "I see you!",
    "Stroke the screen, it feels good!",
    "Where's my fish?",
    "I wish I could eat...",
    "Give me a piece of food!",
    "are you here?",
    "I didn't break it!",
    "Did you forget about me?",
    "hmmm..."
]

sleep = 7

cat_face = random.choice(cat_faces)

#screen (._.)
def clear_screen():
    os.system('clear')

#cursor  (=^_^=)
def move_cursor(x, y):
    sys.stdout.write(f"\033[{y};{x}H")

def hide_cursor(): 
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

#cat (>_<)
def print_cat():
    for i, line in enumerate(cat_face.split('\n')):
        move_cursor(10, 10 + i)
        print(line, end='', flush=True)

#message (>_<)
def print_message():
    message = random.choice(messages)
    msg_width = len(message) + 4
    msg_height = 3
    msg_box = "+" + "-" * (msg_width - 2) + "+\n"
    msg_box += "| " + message + " |\n"
    msg_box += "+" + "-" * (msg_width - 2) + "+"

    for i, line in enumerate(msg_box.split('\n')):
        move_cursor(10 + len(cat_face.split('\n')[0]) + 2, 8 + i)
        print(line, end='', flush=True)

def main():
    global cat_face

    hide_cursor()
    try:
        while True:
            clear_screen()
            print_cat()
            print_message()
            cat_face = random.choice(cat_faces)
            time.sleep(sleep)
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()

if __name__ == "__main__":
    main()