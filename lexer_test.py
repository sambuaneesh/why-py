import unittest
from lexer import Lexer, TokenType

class TestLexer(unittest.TestCase):
    def test_next_token(self):
        input_code = '''manifest five with 5 seal
manifest ten with 10 seal

manifest add with rune(x knot y) unfold
  x augments y seal
fold seal

manifest result with add(five knot ten) seal
negate diminishes divide conjoins 5 seal
5 descends 10 ascends 5 seal

whence (5 descends 10) unfold
    yield verity seal
fold elsewise unfold
    yield fallacy seal
fold

10 mirrors 10 seal
10 diverges 9 seal
"foobar"
"foo bar"
'''

        tests = [
            (TokenType.LET, "manifest"),
            (TokenType.IDENT, "five"),
            (TokenType.ASSIGN, "with"),
            (TokenType.INT, "5"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.LET, "manifest"),
            (TokenType.IDENT, "ten"),
            (TokenType.ASSIGN, "with"),
            (TokenType.INT, "10"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.LET, "manifest"),
            (TokenType.IDENT, "add"),
            (TokenType.ASSIGN, "with"),
            (TokenType.FUNCTION, "rune"),
            (TokenType.LPAREN, "("),
            (TokenType.IDENT, "x"),
            (TokenType.COMMA, "knot"),
            (TokenType.IDENT, "y"),
            (TokenType.RPAREN, ")"),
            (TokenType.LBRACE, "unfold"),
            (TokenType.IDENT, "x"),
            (TokenType.PLUS, "augments"),
            (TokenType.IDENT, "y"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.RBRACE, "fold"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.LET, "manifest"),
            (TokenType.IDENT, "result"),
            (TokenType.ASSIGN, "with"),
            (TokenType.IDENT, "add"),
            (TokenType.LPAREN, "("),
            (TokenType.IDENT, "five"),
            (TokenType.COMMA, "knot"),
            (TokenType.IDENT, "ten"),
            (TokenType.RPAREN, ")"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.BANG, "negate"),
            (TokenType.MINUS, "diminishes"),
            (TokenType.SLASH, "divide"),
            (TokenType.ASTERISK, "conjoins"),
            (TokenType.INT, "5"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.INT, "5"),
            (TokenType.LT, "descends"),
            (TokenType.INT, "10"),
            (TokenType.GT, "ascends"),
            (TokenType.INT, "5"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.IF, "whence"),
            (TokenType.LPAREN, "("),
            (TokenType.INT, "5"),
            (TokenType.LT, "descends"),
            (TokenType.INT, "10"),
            (TokenType.RPAREN, ")"),
            (TokenType.LBRACE, "unfold"),
            (TokenType.RETURN, "yield"),
            (TokenType.TRUE, "verity"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.RBRACE, "fold"),
            (TokenType.ELSE, "elsewise"),
            (TokenType.LBRACE, "unfold"),
            (TokenType.RETURN, "yield"),
            (TokenType.FALSE, "fallacy"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.RBRACE, "fold"),
            (TokenType.INT, "10"),
            (TokenType.EQ, "mirrors"),
            (TokenType.INT, "10"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.INT, "10"),
            (TokenType.NOT_EQ, "diverges"),
            (TokenType.INT, "9"),
            (TokenType.SEMICOLON, "seal"),
            (TokenType.STRING, "foobar"),
            (TokenType.STRING, "foo bar"),
            (TokenType.EOF, ""),
        ]

        lexer = Lexer(input_code)

        for i, (expected_type, expected_literal) in enumerate(tests):
            token = lexer.next_token()
            
            self.assertEqual(token.type, expected_type, 
                f"tests[{i}] - tokentype wrong. expected={expected_type}, got={token.type}")
            
            self.assertEqual(token.literal, expected_literal, 
                f"tests[{i}] - literal wrong. expected='{expected_literal}', got='{token.literal}'")

if __name__ == '__main__':
    unittest.main()