from lexer import Lexer
from tok import Token, TokenType
from parser import Parser
import os
import platform

RESET = "\033[0m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RED = "\033[31m"

user = os.getlogin() if os.name != 'nt' else os.environ.get('USERNAME')
system_info = platform.system() + " " + platform.release()
prompt1 = f"{GREEN}┌──({CYAN}{user}㉿{system_info}{GREEN})-[{YELLOW}PyFly{GREEN}]\n"
prompt2 = f"└─{MAGENTA}${RESET} "

def print_parser_errors(errors):
    for msg in errors:
        print(f"{RED}└─ Error: {msg}{RESET}")

def start():
    print(f"{YELLOW}Welcome to PyFly{RESET}")
    print(f"{CYAN}Type your code below. Use Ctrl+D to exit.{RESET}\n")

    while True:
        print(prompt1, end="")
        try:
            line = input(prompt2)
        except EOFError:
            print("\nGoodbye!")
            return

        lexer = Lexer(line)
        parser = Parser(lexer)
        program = parser.parse_program()

        if len(parser.errors) != 0:
            print_parser_errors(parser.errors)
            continue

        print(f"{GREEN}└─ {program.string()}{RESET}")
        print()
