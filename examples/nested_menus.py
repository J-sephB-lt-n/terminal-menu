"""
$ python -m examples.multi_page_menu
"""

from terminal_menu import menu

sound_status: str = "On"
video_quality: str = "Low"
persist_menu: bool = True
while persist_menu:
    user_choice: str = menu(
        static_menu_text="-- MAIN MENU --", choices=("New Game", "Options", "Exit")
    )
    if user_choice == "Exit":
        break
    elif user_choice == "New Game":
        user_choice = menu(
            static_menu_text="-- NEW GAME --",
            choices=("Single Player", "Multiplayer", "Back to Main Menu"),
        )
        if user_choice in ("Single Player", "Multiplayer"):
            print(f"User started new {user_choice} game")
            persist_menu = False
    elif user_choice == "Options":
        persist_options_menu: bool = True
        while persist_options_menu:
            user_choice = menu(
                static_menu_text=f"""-- OPTIONS --
Sound is currently {sound_status}
Video quality is currently {video_quality}
""",
                choices=("Sound", "Video", "Back to Main Menu"),
            )
            if user_choice == "Back to Main Menu":
                persist_options_menu = False
            elif user_choice == "Sound":
                user_choice = menu(
                    static_menu_text="-- SOUND OPTIONS --",
                    choices=("Off", "On", "Back to Options"),
                )
                if user_choice in ("Off", "On"):
                    sound_status = user_choice
            elif user_choice == "Video":
                user_choice = menu(
                    static_menu_text="-- VIDEO OPTIONS --",
                    choices=("Low", "Medium", "High", "Back to Options"),
                )
                if user_choice in ("Low", "Medium", "High"):
                    video_quality = user_choice
