import curses
import os


def main(win):
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
        except Exception:
            # No input
            pass


curses.wrapper(main)
