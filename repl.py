from lexer import Lexer
from tok import Token, TokenType

prompt = ">> "

def start():
    print("Welcome to PyFly")
    print("start typing in this repl:")

    while True:
        print(prompt, end="")
        line = input()
        lexer = Lexer(line)
        tok = lexer.next_token()
        while tok.type != TokenType.EOF:
            print(tok)
            tok = lexer.next_token()
