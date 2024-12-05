from object import Integer, Boolean, Null, Error, Function
import unittest
from lexer import Lexer
from parser import Parser
from eval import Eval
from environment import Environment
def test_eval(input):
    l = Lexer(input)
    p = Parser(l)
    program = p.parse_program()
    env = Environment()
    return Eval(program, env)

def test_integer_object(t, obj, expected):
    if not isinstance(obj, Integer):
        t.fail(f"object is not Integer. got={type(obj)} ({obj})")
        return False
    if obj.value != expected.value:
        t.fail(f"object has wrong value. got={obj.value}, want={expected.value}")
        return False
    return True

def test_boolean_object(t, obj, expected):
    if not isinstance(obj, Boolean):
        t.fail(f"object is not Boolean. got={type(obj)} ({obj})")
        return False
    if obj.value != expected:
        t.fail(f"object has wrong value. got={obj.value}, want={expected}")
        return False
    return True

def test_null_object(t, obj):
    if not isinstance(obj, Null):
        t.fail(f"object is not Null. got={type(obj)} ({obj})")
        return False
    return True

class TestObject(unittest.TestCase):
    def test_integer_object(self):
        tests = [
            ("5", Integer(5)),
            ("10", Integer(10)),
            ("-5", Integer(-5)),
            ("-10", Integer(-10)),
            ("5 + 5 + 5 + 5 - 10", Integer(10)),
            ("2 * 2 * 2 * 2 * 2", Integer(32)),
            ("-50 + 100 + -50", Integer(0)),
            ("5 * 2 + 10", Integer(20)),
            ("5 + 2 * 10", Integer(25)),
            ("20 + 2 * -10", Integer(0)),
            ("50 / 2 * 2 + 10", Integer(60)),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_integer_object(self, evaluated, expected)

    def test_boolean_object(self):
        tests = [
            ("true", True),
            ("false", False),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_boolean_object(self, evaluated, expected)

    def test_bang_operator(self):
        tests = [
            ("!true", False),
            ("!false", True),
            ("!5", False),
            ("!!true", True),
            ("!!false", False),
            ("!!5", True),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_boolean_object(self, evaluated, expected)

    def test_eval_boolean_expression(self):
        tests = [
            ("true", True),
            ("false", False),
            ("1 < 2", True),
            ("1 > 2", False),
            ("1 < 1", False),
            ("1 > 1", False),
            ("1 == 1", True),
            ("1 != 1", False),
            ("true == true", True),
            ("false == false", True),
            ("true == false", False),
            ("true != false", True),
            ("false != true", True),
            ("(1 < 2) == true", True),
            ("(1 < 2) == false", False),
            ("(1 > 2) == true", False),
            ("(1 > 2) == false", True),
        ]

        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_boolean_object(self, evaluated, expected)

    def test_if_else_expressions(self):
        tests = [
            ("if (true) { 10 }", 10),
            ("if (false) { 10 }", None),
            ("if (1) { 10 }", 10),
            ("if (1 < 2) { 10 }", 10),
            ("if (1 > 2) { 10 }", None),
            ("if (1 > 2) { 10 } else { 20 }", 20),
            ("if (1 < 2) { 10 } else { 20 }", 10),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                if expected is None:
                    test_null_object(self, evaluated)
                else:
                    test_integer_object(self, evaluated, Integer(expected))

    def test_return_statements(self):
        tests = [
            ("return 10;", 10),
            ("return 10; 9;", 10),
            ("return 2 * 5; 9;", 10),
            ("9; return 2 * 5; 9;", 10),
            ("if (10 > 1) { return 10; }", 10),
            ("if (10 > 1) { if (10 > 1) { return 10; } return 1; }", 10),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_integer_object(self, evaluated, Integer(expected))

    def test_error_handling(self):
        tests = [
            ("5 + true;", "type mismatch: INTEGER + BOOLEAN"),
            ("5 + true; 5;", "type mismatch: INTEGER + BOOLEAN"), 
            ("-true", "unknown operator: -BOOLEAN"),
            ("true + false;", "unknown operator: BOOLEAN + BOOLEAN"),
            ("5; true + false; 5", "unknown operator: BOOLEAN + BOOLEAN"),
            ("if (10 > 1) { true + false; }", "unknown operator: BOOLEAN + BOOLEAN"),
            ("""
if (10 > 1) {
    if (10 > 1) {
        return true + false;
    }
    return 1;
}
""", "unknown operator: BOOLEAN + BOOLEAN"),
        ]

        for (input, expected_message) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                self.assertIsInstance(evaluated, Error)
                self.assertEqual(evaluated.message, expected_message)

    def test_let_statements(self):
        tests = [
            ("let a = 5; a;", 5),
            ("let a = 5 * 5; a;", 25), 
            ("let a = 5; let b = a; b;", 5),
            ("let a = 5; let b = a; let c = a + b + 5; c;", 15),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_integer_object(self, evaluated, Integer(expected))

    def test_function_object(self):
        input = "fn(x) { x + 2; };"
        evaluated = test_eval(input)
        self.assertIsInstance(evaluated, Function)
        fn = evaluated
        
        self.assertEqual(len(fn.parameters), 1, 
            f"function has wrong parameters. Parameters={fn.parameters}")
            
        self.assertEqual(fn.parameters[0].token_literal(), "x",
            f"parameter is not 'x'. got={fn.parameters[0].token_literal()}")
            
        expected_body = "(x + 2)"
        self.assertEqual(fn.body.string(), expected_body,
            f"body is not {expected_body}. got={fn.body.string()}")

if __name__ == "__main__":
    unittest.main()
