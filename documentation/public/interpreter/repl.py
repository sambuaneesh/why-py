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
prompt1 = f"{GREEN}┌──({CYAN}Ancient One {user}'s{GREEN})-[{YELLOW}Grimoire{GREEN}]\n"
prompt2 = f"└─{MAGENTA}⚡{RESET} "
continuation_prompt = f"{GREEN}│ {MAGENTA}...{RESET} "

def print_parser_errors(errors):
    for msg in errors:
        print(f"{RED}└─ Arcane Error: {msg}{RESET}")

def is_complete_expression(lines):
    """Check if the input forms a complete expression."""
    source = " ".join(line.strip() for line in lines)
    
    # Count block delimiters
    unfold_count = source.count("unfold")
    fold_count = source.count("fold")
    
    # If we're in a block (have unfold)
    if unfold_count > 0:
        # Need matching folds and must end with 'fold seal'
        return unfold_count == fold_count and source.strip().endswith("fold seal")
    
    # If no blocks, just check for seal termination
    return source.strip().endswith("seal")

def read_multiline_input():
    """Read multiline input until a complete expression is formed."""
    lines = []
    buffer = ""
    print(prompt1, end="")  # Print the initial prompt
    
    while True:
        try:
            if not lines:
                line = input(prompt2)
            else:
                line = input(continuation_prompt)
            
            if not line.strip() and not lines:  # Skip empty initial lines
                print(prompt1, end="")
                continue
                
            lines.append(line)
            buffer = "\n".join(lines)
            
            # Check if we have a complete expression
            if is_complete_expression(lines):
                return buffer
                
        except EOFError:
            if buffer.strip():
                return buffer
            raise
        except KeyboardInterrupt:
            if lines:  # If we're in the middle of input
                lines = []  # Clear the current input
                buffer = ""
                print("\nIncantation cancelled.")
                print(prompt1, end="")
            else:
                raise

def start(in_stream=sys.stdin, out_stream=sys.stdout):
    env = Environment()
    print(f"\n{YELLOW}╭──────────────────────────────────────────────╮{RESET}", file=out_stream)
    print(f"{YELLOW}│   Hark, Wanderer of the Digital Planes...    │{RESET}", file=out_stream)
    print(f"{YELLOW}│   Enter ye the Ancient REPL of whyPY         │{RESET}", file=out_stream)
    print(f"{YELLOW}╰──────────────────────────────────────────────╯{RESET}", file=out_stream)
    print(file=out_stream)
    print(f"{CYAN}Sacred Instructions:{RESET}", file=out_stream)
    print(f"{CYAN}  • Inscribe your mystical runes (ancient scrolls welcome){RESET}", file=out_stream)
    print(f"{CYAN}  • Ctrl+D - Part the veils between realms{RESET}", file=out_stream)
    print(f"{CYAN}  • Ctrl+C - Banish the current incantation{RESET}\n", file=out_stream)

    while True:
        try:
            source = read_multiline_input()
            if not source.strip():
                continue

            lexer = Lexer(source)
            parser = Parser(lexer)
            program = parser.parse_program()

            if len(parser.errors) != 0:
                print_parser_errors(parser.errors)
                continue

            evaluated = Eval(program, env)
            if evaluated is not None:
                print(f"{GREEN}└─ The runes speak: {evaluated.inspect()}{RESET}", file=out_stream)
                print(file=out_stream)

        except KeyboardInterrupt:
            print("\nIncantation cancelled.", file=out_stream)
            continue
        except EOFError:
            print("\nMay your code forever flow in the streams of time!", file=out_stream)
            return
