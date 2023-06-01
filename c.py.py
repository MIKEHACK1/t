import os
import sys
import time
from colorama import init, Fore, Back, Style

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def print_colored_text(text, color):
    print(color + text + Style.RESET_ALL, end='')

def print_rainbow_3d_m():
    clear_console()
    init()

    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    m = [
        "M        M",
        "MM      MM",
        "M M    M M",
        "M  M  M  M",
        "M   MM   M",
        "M        M",
        "M        M",
        "M        M"
    ]

    for i, row in enumerate(m):
        for char in row:
            color = colors[i % len(colors)]
            print_colored_text(char, color)
        print()

    time.sleep(2)

print_rainbow_3d_m()
