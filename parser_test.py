from lexer import Lexer
from ast1 import *
from parser import Parser

import unittest

class TestParser(unittest.TestCase):
    def test_let_statements(self):
        input = """
let x = 6;
let y = 9;
let xy = 69;
"""
        lexer = Lexer(input)
        parser = Parser(lexer)
        program = parser.parse_program()
        self._check_parser_errors(parser)

        if program is None:
            self.fail("parse_program() returned None")

        if len(program.statements) != 3:
            self.fail(f"program.statements does not contain 3 statements. got={len(program.statements)}")

        tests = [
            {"expected_identifier": "x"},
            {"expected_identifier": "y"}, 
            {"expected_identifier": "xy"}
        ]

        for i, tt in enumerate(tests):
            stmt = program.statements[i]
            self.assertTrue(self._test_let_statement(stmt, tt["expected_identifier"]))

    def _check_parser_errors(self, parser: Parser):
        errors = parser.errors
        if len(errors) == 0:
            return
        
        print("parser has {len(errors)} errors:")
        for msg in errors:
            print(f"parser error: {msg}")
        self.fail("parser had errors")

    def _test_let_statement(self, stmt: LetStatement, name: str) -> bool:
        if stmt.token_literal() != "let":
            self.fail(f"stmt.token_literal not 'let'. got={stmt.token_literal()}")
            return False

        if not isinstance(stmt, LetStatement):
            self.fail(f"stmt not LetStatement. got={type(stmt)}")
            return False

        if stmt.name.value != name:
            self.fail(f"stmt.name.value not '{name}'. got={stmt.name.value}")
            return False

        if stmt.name.token_literal() != name:
            self.fail(f"stmt.name.token_literal() not '{name}'. got={stmt.name.token_literal()}")
            return False

        return True
    
    def test_return_statements(self):
        input = """
return 6;
return 9;
return 69;
"""
        lexer = Lexer(input)
        parser = Parser(lexer)
        program = parser.parse_program()
        self._check_parser_errors(parser)

        if len(program.statements) != 3:
            self.fail(f"program.statements does not contain 3 statements. got={len(program.statements)}")

        for stmt in program.statements:
            if not isinstance(stmt, ReturnStatement):
                self.fail(f"stmt not ReturnStatement. got={type(stmt)}")
                continue

            if stmt.token_literal() != "return":
                self.fail(f"returnStmt.token_literal not 'return', got {stmt.token_literal()}")

    def test_identifier_expression(self):
        input = "sixtynine;"
        
        lexer = Lexer(input)
        parser = Parser(lexer)
        program = parser.parse_program()
        self._check_parser_errors(parser)

        if len(program.statements) != 1:
            self.fail(f"program has not enough statements. got={len(program.statements)}")

        stmt = program.statements[0]
        if not isinstance(stmt, ExpressionStatement):
            self.fail(f"program.statements[0] is not ExpressionStatement. got={type(stmt)}")

        ident = stmt.expression
        if not isinstance(ident, Identifier):
            self.fail(f"exp not Identifier. got={type(ident)}")

        if ident.value != "sixtynine":
            self.fail(f"ident.value not sixtynine. got={ident.value}")

        if ident.token_literal() != "sixtynine":
            self.fail(f"ident.token_literal not sixtynine. got={ident.token_literal()}")

    def test_integer_literal_expression(self):
        input = "69;"
        
        lexer = Lexer(input)
        parser = Parser(lexer)
        program = parser.parse_program()
        self._check_parser_errors(parser)

        if len(program.statements) != 1:
            self.fail(f"program has not enough statements. got={len(program.statements)}")

        stmt = program.statements[0]
        if not isinstance(stmt, ExpressionStatement):
            self.fail(f"program.statements[0] is not ExpressionStatement. got={type(stmt)}")

        if not self._test_literal_expression(stmt.expression, 69):
            return

    def _test_literal_expression(self, exp: Expression, expected) -> bool:
        if isinstance(expected, int):
            return self._test_integer_literal(exp, expected)
        elif isinstance(expected, bool):
            return self._test_boolean_literal(exp, expected)
        self.fail(f"type of exp not handled. got={type(exp)}")
        return False

    def _test_boolean_literal(self, exp: Expression, value: bool) -> bool:
        if not isinstance(exp, Boolean):
            self.fail(f"exp not Boolean. got={type(exp)}")
            return False
        
        if exp.value != value:
            self.fail(f"bo.value not {value}. got={exp.value}")
            return False

        if exp.token_literal() != str(value).lower():
            self.fail(f"bo.token_literal not {value}. got={exp.token_literal()}")
            return False

        return True

    def test_parsing_prefix_expressions(self):
        prefix_tests = [
            ("!69;", "!", 69),
            ("-169;", "-", 169),
        ]

        for input, operator, integer_value in prefix_tests:
            lexer = Lexer(input)
            parser = Parser(lexer)
            program = parser.parse_program()
            self._check_parser_errors(parser)

            if len(program.statements) != 1:
                self.fail(f"program.statements does not contain 1 statements. got={len(program.statements)}")

            stmt = program.statements[0]
            if not isinstance(stmt, ExpressionStatement):
                self.fail(f"program.statements[0] is not ExpressionStatement. got={type(stmt)}")

            exp = stmt.expression
            if not isinstance(exp, PrefixExpression):
                self.fail(f"stmt is not PrefixExpression. got={type(exp)}")

            if exp.operator != operator:
                self.fail(f"exp.operator is not '{operator}'. got={exp.operator}")

            if not self._test_integer_literal(exp.right, integer_value):
                return

    def _test_integer_literal(self, il, value):
        if not isinstance(il, IntegerLiteral):
            self.fail(f"il not *IntegerLiteral. got={type(il)}")
            return False

        if il.value != value:
            self.fail(f"integ.Value not {value}. got={il.value}")
            return False

        if il.token_literal() != str(value):
            self.fail(f"integ.TokenLiteral not {value}. got={il.token_literal()}")
            return False

        return True

    def _test_identifier(self, exp, value):
        if not isinstance(exp, Identifier):
            self.fail(f"exp not Identifier. got={type(exp)}")
            return False

        if exp.value != value:
            self.fail(f"ident.Value not {value}. got={exp.value}")
            return False

        if exp.token_literal() != value:
            self.fail(f"ident.TokenLiteral not {value}. got={exp.token_literal()}")
            return False

        return True

    def _test_literal_expression(self, exp, expected):
        if isinstance(expected, int):
            return self._test_integer_literal(exp, expected)
        elif isinstance(expected, str):
            return self._test_identifier(exp, expected)
        self.fail(f"type of exp not handled. got={type(exp)}")
        return False

    def _test_infix_expression(self, exp, left, operator, right):
        if not isinstance(exp, InfixExpression):
            self.fail(f"exp is not InfixExpression. got={type(exp)}")
            return False

        if not self._test_literal_expression(exp.left, left):
            return False

        if exp.operator != operator:
            self.fail(f"exp.operator is not '{operator}'. got={exp.operator}")
            return False

        if not self._test_literal_expression(exp.right, right):
            return False

        return True
    
    def test_parsing_infix_expressions(self):
        infix_tests = [
            ("69 + 69;", 69, "+", 69),
            ("69 - 69;", 69, "-", 69), 
            ("69 * 69;", 69, "*", 69),
            ("69 / 69;", 69, "/", 69),
            ("69 > 69;", 69, ">", 69),
            ("69 < 69;", 69, "<", 69),
            ("69 == 69;", 69, "==", 69),
            ("69 != 69;", 69, "!=", 69),
        ]

        for input, left_value, operator, right_value in infix_tests:
            lexer = Lexer(input)
            parser = Parser(lexer)
            program = parser.parse_program()
            self._check_parser_errors(parser)

            if len(program.statements) != 1:
                self.fail(f"program.statements does not contain 1 statement. got={len(program.statements)}")

            stmt = program.statements[0]
            if not isinstance(stmt, ExpressionStatement):
                self.fail(f"program.statements[0] is not ExpressionStatement. got={type(stmt)}")

            exp = stmt.expression
            if not isinstance(exp, InfixExpression):
                self.fail(f"exp is not InfixExpression. got={type(exp)}")

            if not self._test_integer_literal(exp.left, left_value):
                return

            if exp.operator != operator:
                self.fail(f"exp.operator is not '{operator}'. got={exp.operator}")

            if not self._test_integer_literal(exp.right, right_value):
                return
            
    def test_operator_precedence_parsing(self):
        tests = [
            {
                "input": "-a * b",
                "expected": "((-a) * b)"
            },
            {
                "input": "!-a",
                "expected": "(!(-a))"
            },
            {
                "input": "a + b + c",
                "expected": "((a + b) + c)"
            },
            {
                "input": "a + b - c", 
                "expected": "((a + b) - c)"
            },
            {
                "input": "a * b * c",
                "expected": "((a * b) * c)"
            },
            {
                "input": "a * b / c",
                "expected": "((a * b) / c)"
            },
            {
                "input": "a + b / c",
                "expected": "(a + (b / c))"
            },
            {
                "input": "a + b * c + d / e - f",
                "expected": "(((a + (b * c)) + (d / e)) - f)"
            },
            {
                "input": "3 + 4; -5 * 5",
                "expected": "(3 + 4)((-5) * 5)"
            },
            {
                "input": "5 > 4 == 3 < 4",
                "expected": "((5 > 4) == (3 < 4))"
            },
            {
                "input": "5 < 4 != 3 > 4",
                "expected": "((5 < 4) != (3 > 4))"
            },
            {
                "input": "3 + 4 * 5 == 3 * 1 + 4 * 5",
                "expected": "((3 + (4 * 5)) == ((3 * 1) + (4 * 5)))"
            },
            {
                "input": "true",
                "expected": "true"
            },
            {
                "input": "false", 
                "expected": "false"
            },
            {
                "input": "3 > 5 == false",
                "expected": "((3 > 5) == false)"
            },
            {
                "input": "3 < 5 == true",
                "expected": "((3 < 5) == true)"
            },
            {
                "input": "1 + (2 + 3) + 4",
                "expected": "((1 + (2 + 3)) + 4)"
            },
            {
                "input": "(5 + 5) * 2",
                "expected": "((5 + 5) * 2)"
            },
            {
                "input": "2 / (5 + 5)",
                "expected": "(2 / (5 + 5))"
            },
            {
                "input": "-(5 + 5)",
                "expected": "(-(5 + 5))"
            },
            {
                "input": "!(true == true)",
                "expected": "(!(true == true))"
            }
        ]

        for tt in tests:
            lexer = Lexer(tt.get("input"))
            parser = Parser(lexer)
            program = parser.parse_program()
            self._check_parser_errors(parser)

            actual = program.string()
            if actual != tt.get("expected"):
                self.fail(f"expected={tt.get('expected')}, got={actual}")

if __name__ == "__main__":
    unittest.main()