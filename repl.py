from lexer import Lexer
from tok import Token, TokenType
from parser import Parser
from eval import Eval
from environment import Environment
import os
import platform
import sys

RESET = "\033[0m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RED = "\033[31m"

user = os.getlogin() if os.name != 'nt' else os.environ.get('USERNAME')
system_info = platform.system() + " " + platform.release()
prompt1 = f"{GREEN}┌──({CYAN}Mystic {user}⚡{system_info}{GREEN})-[{YELLOW}Grimoire{GREEN}]\n"
prompt2 = f"└─{MAGENTA}⚡{RESET} "

def print_parser_errors(errors):
    for msg in errors:
        print(f"{RED}└─ Arcane Error: {msg}{RESET}")

def start(in_stream=sys.stdin, out_stream=sys.stdout):
    env = Environment()
    print(f"{YELLOW}Welcome to the WhyPy{RESET}", file=out_stream)
    print(f"{CYAN}Inscribe your incantations below. Use the sacred Ctrl+D to close the tome.{RESET}\n", file=out_stream)

    while True:
        print(prompt1, end="", file=out_stream)
        try:
            line = input(prompt2)
        except EOFError:
            print("\nMay your code forever flow in the streams of time!", file=out_stream)
            return

        lexer = Lexer(line)
        parser = Parser(lexer)
        program = parser.parse_program()

        if len(parser.errors) != 0:
            print_parser_errors(parser.errors)
            continue

        evaluated = Eval(program, env)
        if evaluated is not None:
            print(f"{GREEN}└─ The runes speak: {evaluated.inspect()}{RESET}", file=out_stream)
            print(file=out_stream)
