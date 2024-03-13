import curses
import os

user_input = {"user_input":None}

def main(win, user_input):
    win.nodelay(True)
    key = ""
    win.clear()
    win.addstr("Detected key:")

    while True:
        try:
            key = win.getkey()
            win.clear()
            win.addstr("Detected key:")
            win.addstr(str(key))
            if key == os.linesep:
                break
            user_input["user_input"] = str(key)
            break
        except Exception:
            # No input
            pass

curses.wrapper(main, user_input=user_input)
print(user_input)

