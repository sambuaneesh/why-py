from lexer import Lexer
from ast1 import *
from parser import Parser

import unittest

class TestParser(unittest.TestCase):
    def test_let_statements(self):
        input = """
manifest x with 6 seal
manifest y with 9 seal
manifest xy with 69 seal
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
        if stmt.token_literal() != "manifest":
            self.fail(f"stmt.token_literal not 'manifest'. got={stmt.token_literal()}")
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
yield 6 seal
yield 9 seal
yield 69 seal
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

            if stmt.token_literal() != "yield":
                self.fail(f"returnStmt.token_literal not 'yield', got {stmt.token_literal()}")

    def test_identifier_expression(self):
        input = "sixtynine seal"
        
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
        input = "69 seal"
        
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
        if not isinstance(exp, BooleanLiteral):
            self.fail(f"exp not Boolean. got={type(exp)}")
            return False
        
        if exp.value != value:
            self.fail(f"bo.value not {value}. got={exp.value}")
            return False

        expected_literal = "verity" if value else "fallacy"
        if exp.token_literal() != expected_literal:
            self.fail(f"bo.token_literal not {expected_literal}. got={exp.token_literal()}")
            return False

        return True

    def test_parsing_prefix_expressions(self):
        prefix_tests = [
            ("negate 69 seal", "negate", 69),
            ("diminishes 169 seal", "diminishes", 169),
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
            ("69 augments 69 seal", 69, "augments", 69),
            ("69 diminishes 69 seal", 69, "diminishes", 69), 
            ("69 conjoins 69 seal", 69, "conjoins", 69),
            ("69 divide 69 seal", 69, "divide", 69),
            ("69 ascends 69 seal", 69, "ascends", 69),
            ("69 descends 69 seal", 69, "descends", 69),
            ("69 mirrors 69 seal", 69, "mirrors", 69),
            ("69 diverges 69 seal", 69, "diverges", 69),
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
                "input": "diminishes a conjoins b",
                "expected": "((diminishes a) conjoins b)"
            },
            {
                "input": "negate diminishes a",
                "expected": "(negate (diminishes a))"
            },
            {
                "input": "a augments b augments c",
                "expected": "((a augments b) augments c)"
            },
            {
                "input": "a augments b diminishes c", 
                "expected": "((a augments b) diminishes c)"
            },
            {
                "input": "a conjoins b conjoins c",
                "expected": "((a conjoins b) conjoins c)"
            },
            {
                "input": "a conjoins b divide c",
                "expected": "((a conjoins b) divide c)"
            },
            {
                "input": "a augments b divide c",
                "expected": "(a augments (b divide c))"
            },
            {
                "input": "a augments b conjoins c augments d divide e diminishes f",
                "expected": "(((a augments (b conjoins c)) augments (d divide e)) diminishes f)"
            },
            {
                "input": "3 augments 4 seal diminishes 5 conjoins 5",
                "expected": "(3 augments 4)((diminishes 5) conjoins 5)"
            },
            {
                "input": "5 ascends 4 mirrors 3 descends 4",
                "expected": "((5 ascends 4) mirrors (3 descends 4))"
            },
            {
                "input": "5 descends 4 diverges 3 ascends 4",
                "expected": "((5 descends 4) diverges (3 ascends 4))"
            },
            {
                "input": "3 augments 4 conjoins 5 mirrors 3 conjoins 1 augments 4 conjoins 5",
                "expected": "((3 augments (4 conjoins 5)) mirrors ((3 conjoins 1) augments (4 conjoins 5)))"
            },
            {
                "input": "verity",
                "expected": "verity"
            },
            {
                "input": "fallacy", 
                "expected": "fallacy"
            },
            {
                "input": "3 ascends 5 mirrors fallacy",
                "expected": "((3 ascends 5) mirrors fallacy)"
            },
            {
                "input": "3 descends 5 mirrors verity",
                "expected": "((3 descends 5) mirrors verity)"
            },
            {
                "input": "1 augments (2 augments 3) augments 4",
                "expected": "((1 augments (2 augments 3)) augments 4)"
            },
            {
                "input": "(5 augments 5) conjoins 2",
                "expected": "((5 augments 5) conjoins 2)"
            },
            {
                "input": "2 divide (5 augments 5)",
                "expected": "(2 divide (5 augments 5))"
            },
            {
                "input": "diminishes (5 augments 5)",
                "expected": "(diminishes (5 augments 5))"
            },
            {
                "input": "negate (verity mirrors verity)",
                "expected": "(negate (verity mirrors verity))"
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

    def test_if_expression(self):
        input = "whence (x descends y) unfold x fold"
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
        if not isinstance(exp, IfExpression):
            self.fail(f"stmt.expression is not IfExpression. got={type(exp)}")

        if not self._test_infix_expression(exp.condition, "x", "descends", "y"):
            return

        if len(exp.consequence.statements) != 1:
            self.fail(f"consequence is not 1 statements. got={len(exp.consequence.statements)}")

        consequence = exp.consequence.statements[0]
        if not isinstance(consequence, ExpressionStatement):
            self.fail(f"statements[0] is not ExpressionStatement. got={type(consequence)}")

        if not self._test_identifier(consequence.expression, "x"):
            return

        if exp.alternative is not None:
            self.fail(f"exp.alternative was not None. got={exp.alternative}")

    def test_function_literal_parsing(self):
        input = "rune(x knot y) unfold x augments y seal fold"
        lexer = Lexer(input)
        parser = Parser(lexer)
        program = parser.parse_program()
        self._check_parser_errors(parser)

        if len(program.statements) != 1:
            self.fail(f"program.statements does not contain 1 statements. got={len(program.statements)}")

        stmt = program.statements[0]
        if not isinstance(stmt, ExpressionStatement):
            self.fail(f"program.statements[0] is not ExpressionStatement. got={type(stmt)}")

        function = stmt.expression
        if not isinstance(function, FunctionLiteral):
            self.fail(f"stmt.expression is not FunctionLiteral. got={type(function)}")

        if len(function.parameters) != 2:
            self.fail(f"function literal parameters wrong. want 2, got={len(function.parameters)}")

        self._test_literal_expression(function.parameters[0], "x")
        self._test_literal_expression(function.parameters[1], "y")

        if len(function.body.statements) != 1:
            self.fail(f"function.body.statements has not 1 statements. got={len(function.body.statements)}")

        body_stmt = function.body.statements[0]
        if not isinstance(body_stmt, ExpressionStatement):
            self.fail(f"function body stmt is not ExpressionStatement. got={type(body_stmt)}")

        self._test_infix_expression(body_stmt.expression, "x", "augments", "y")

    def test_function_parameter_parsing(self):
        tests = [
            {"input": "rune() unfold fold seal", "expected_params": []},
            {"input": "rune(x) unfold fold seal", "expected_params": ["x"]},
            {"input": "rune(x knot y knot z) unfold fold seal", "expected_params": ["x", "y", "z"]},
        ]

        for test in tests:
            lexer = Lexer(test["input"])
            parser = Parser(lexer)
            program = parser.parse_program()
            self._check_parser_errors(parser)

            stmt = program.statements[0]
            if not isinstance(stmt, ExpressionStatement):
                self.fail(f"program.statements[0] is not ExpressionStatement. got={type(stmt)}")

            function = stmt.expression
            if not isinstance(function, FunctionLiteral):
                self.fail(f"stmt.expression is not FunctionLiteral. got={type(function)}")

            if len(function.parameters) != len(test["expected_params"]):
                self.fail(
                    f"length parameters wrong. want {len(test['expected_params'])}, "
                    f"got={len(function.parameters)}"
                )

            for i, expected_param in enumerate(test["expected_params"]):
                self._test_literal_expression(function.parameters[i], expected_param)

    def test_call_expression_parsing(self):
        input_text = "add(1 knot 2 conjoins 3 knot 4 augments 5) seal"
        lexer = Lexer(input_text)
        parser = Parser(lexer)
        program = parser.parse_program()
        self._check_parser_errors(parser)

        if len(program.statements) != 1:
            self.fail(
                f"program.statements does not contain 1 statements. got={len(program.statements)}"
            )

        stmt = program.statements[0]
        if not isinstance(stmt, ExpressionStatement):
            self.fail(f"stmt is not ExpressionStatement. got={type(stmt)}")

        exp = stmt.expression
        if not isinstance(exp, CallExpression):
            self.fail(f"stmt.expression is not CallExpression. got={type(exp)}")

        self._test_identifier(exp.function, "add")

        if len(exp.arguments) != 3:
            self.fail(f"wrong length of arguments. got={len(exp.arguments)}")

        self._test_literal_expression(exp.arguments[0], 1)
        self._test_infix_expression(exp.arguments[1], 2, "conjoins", 3)
        self._test_infix_expression(exp.arguments[2], 4, "augments", 5)

if __name__ == "__main__":
    unittest.main()