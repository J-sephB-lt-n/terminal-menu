import curses
import os
from typing import Iterator


class BackForthCycler:
    """Wraps a list (or other iterator), allowing you to step back and forth through it

    Example:
        >>> mylist = ["cat", "pig", "cow"]
        >>> cycler = BackForthCycler(mylist)
        >>> cycler.forth()
        'cat'
        >>> cycler.back()
        'cow'
        >>> cycler.back()
        'pig'
        >>> cycler.forth()
        'cow'
        >>> cycler.forth()
        'cat'
    """

    def __init__(self, iterator: Iterator):
        """TODO"""
        self.iterator: Iterator = iterator
        self.current_idx: int = len(self.iterator) - 1

    def back(self):
        """Returns the previous element in the iterator"""
        if self.current_idx == 0:
            self.current_idx = len(self.iterator) - 1
        else:
            self.current_idx -= 1
        return self.iterator[self.current_idx]

    def forth(self):
        """Returns the next element in the iterator"""
        if self.current_idx == (len(self.iterator) - 1):
            self.current_idx = 0
        else:
            self.current_idx += 1
        return self.iterator[self.current_idx]


def menu(menu_text: str, choices: list[str]) -> str:
    """TODO"""

    def menu_state_string(choices: list[str], selected_idx: int) -> None:
        """TODO"""
        menu_state_string: str = ""
        for idx, choice in enumerate(choices):
            if idx == selected_idx:
                menu_state_string += f"[ {choice} ]\n"
            else:
                menu_state_string += f"  {choice}\n"
        return menu_state_string

    menu_state: dict[str, str] = {"user_choice": None}

    def session(win, menu_state: dict[str, str], choices=list[str]) -> None:
        """TODO"""
        cycler: BackForthCycler = BackForthCycler(range(len(choices)))
        current_selected_idx: int = cycler.forth()
        win.nodelay(True)
        win.clear()
        win.addstr(menu_text + "\n")
        win.addstr(menu_state_string(choices, current_selected_idx))
        while True:
            try:
                key_pressed = win.getkey()
                win.clear()
                win.addstr(menu_text + "\n")
                win.addstr(menu_state_string(choices, current_selected_idx))
                if key_pressed == "KEY_DOWN":
                    current_selected_idx: int = cycler.forth()
                elif key_pressed == "KEY_UP":
                    current_selected_idx: int = cycler.back()
                if key_pressed == os.linesep:
                    menu_state["user_choice"] = choices[current_selected_idx]
            except curses.error:
                # i.e. no keypress detected #
                pass

    curses.wrapper(session, menu_state=menu_state, choices=choices)

    return menu_state("user_choice")
