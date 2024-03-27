"""
Code for creating a terminal menu
"""

import curses
import os
from typing import Iterator


class BackForthCycler:
    """Walks back and forth through a list (or other iterator)

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
        """Sets attributes at instantiation of the class"""
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


def menu(static_menu_text: str, choices: tuple[str, ...]) -> str:
    """Runs a persistent menu in the terminal

    Notes:
        The python curses library only works on unix machines (on windows, it will work on WSL)

    Args:
        static_menu_text (str): Text to display at the top of the menu
        choices (tuple[str, ...]): Menu items from which the user can select

    Returns:
        string: The item (from `choices`) which the user selected
    """
    _menu_state: dict[str, str | None] = {"user_choice": None}

    def session(win, _menu_state: dict[str, str], _choices=tuple[str, ...]) -> None:
        """Creates and manages the menu

        Args:
            win (TODO): TODO
            _menu_state (dict[str, str|None]): Persistent object used to store the user choice
            _choices (tuple[str, ...]): Menu items from which the user can select
        """
        cycler: BackForthCycler = BackForthCycler(range(len(_choices)))
        current_selected_idx: int = cycler.forth()

        max_choice_len: int = max([len(choice) for choice in _choices])

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        BLACK_WHITE = curses.color_pair(1)

        win.nodelay(True)
        win.clear()
        win.addstr(static_menu_text + "\n")
        for choice_idx, choice in enumerate(_choices):
            if choice_idx == current_selected_idx:
                win.addstr(f" {choice:<{max_choice_len+1}}\n", BLACK_WHITE)
            else:
                win.addstr(f" {choice}\n")
        while True:
            try:
                key_pressed = win.getkey()
                win.clear()
                if key_pressed == "KEY_DOWN":
                    current_selected_idx = cycler.forth()
                elif key_pressed == "KEY_UP":
                    current_selected_idx = cycler.back()
                if key_pressed == os.linesep:
                    _menu_state["user_choice"] = _choices[current_selected_idx]
                    break
                win.addstr(static_menu_text + "\n")
                for choice_idx, choice in enumerate(_choices):
                    if choice_idx == current_selected_idx:
                        win.addstr(f" {choice:<{max_choice_len+1}}\n", BLACK_WHITE)
                    else:
                        win.addstr(f" {choice}\n")
            except curses.error:
                # i.e. no keypress detected #
                pass

    curses.wrapper(session, _menu_state=_menu_state, _choices=choices)

    return _menu_state["user_choice"]
