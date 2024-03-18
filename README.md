# Terminal Menu using Python 

```python
from terminal_menu import menu
user_choice: str = menu(
    static_menu_text="Please choose an annoying little dog:",
    choices=("Chihuahua", "Pomeranian", "Jack Russell"),
)
print(f"user chose '{user_choice}'")
```

![](./examples/gifs/basic_menu.gif)

I wanted a simple OS-agnostic interface for creating menus in my python command-line applications (using only the python standard library). 

I could not find one that I liked, so I built this one. 

It is not truly operating system agnostic since it uses the [curses](https://docs.python.org/3/library/curses.html#module-curses) python library, which will not work on a Windows terminal. It works on WSL though.

I purposely contained all of the functionality in a single script ([terminal_menu.py](./terminal_menu.py)) which you can easily include in your own project, but if you don't mind your project looking like a NodeJS project, then you can also install this code from [pyPI](https://pypi.org/project/terminal-menu/):

```bash
pip install terminal-menu
```
