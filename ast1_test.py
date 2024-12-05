import unittest
from ast1 import Program, LetStatement, Identifier, IntegerLiteral
from tok import Token, TokenType

class TestAST(unittest.TestCase):
    def test_string(self):
        program = Program(
            statements=[
                LetStatement(
                    token=Token(type=TokenType.LET, literal="let"),
                    name=Identifier(
                        token=Token(type=TokenType.IDENT, literal="xy"),
                        value="xy"
                    ),
                    value=IntegerLiteral(
                        token=Token(type=TokenType.INT, literal="69"), 
                        value=69
                    )
                )
            ]
        )

        expected = "let xy = 69;"
        if program.string() != expected:
            print(f"program.string() wrong. got={program.string()}")
            assert False

if __name__ == "__main__":
    unittest.main()