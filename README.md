# Menu Interface for Terminal-Based Python Applications 

I wanted a simple OS-agnostic interface for creating menus in my python command-line applications (using only the python standard library). 

I could not find one that I liked, so I built this one. 

It is not truly operating system agnostic since it uses the [curses](https://docs.python.org/3/library/curses.html#module-curses) python library, which will not work on a Windows terminal. It works on WSL though.
