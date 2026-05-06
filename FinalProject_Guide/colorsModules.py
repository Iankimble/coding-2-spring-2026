from colorama import init, Fore, Back, Style

# Required on Windows, harmless on Mac/Linux
init(autoreset=True)  # autoreset means each print resets back to normal automatically

# --- Basic Colors ---
print(Fore.RED    + "This text is red")
print(Fore.GREEN  + "This text is green")
print(Fore.YELLOW + "This text is yellow")
print(Fore.BLUE   + "This text is blue")
print(Fore.CYAN   + "This text is cyan")

# --- Background Colors ---
print(Back.RED   + "This has a red background")
print(Back.GREEN + Fore.BLACK + "Green background, black text")

# --- Text Style ---
print(Style.BRIGHT + "This text is bright/bold")
print(Style.DIM    + "This text is dimmed")

# --- Combining them ---
print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + "Yellow bold text on blue background")