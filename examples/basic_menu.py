"""
Example of an extremely basic terminal menu

$ python -m examples.basic_menu
"""

from terminal_menu import menu

user_choice: str = menu(
    static_menu_text="Please choose an annoying little dog:",
    choices=("Chihuahua", "Pomeranian", "Jack Russell"),
)
print(f"user chose '{user_choice}'")
