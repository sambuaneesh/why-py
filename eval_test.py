from object import Integer, Boolean, Null, Error, Function, String
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
        t.fail(f"object is not NUMBER. got={type(obj)} ({obj})")
        return False
    if obj.value != expected.value:
        t.fail(f"object has wrong value. got={obj.value}, want={expected.value}")
        return False
    return True

def test_boolean_object(t, obj, expected):
    if not isinstance(obj, Boolean):
        t.fail(f"object is not TRUTH. got={type(obj)} ({obj})")
        return False
    if obj.value != expected:
        t.fail(f"object has wrong value. got={obj.value}, want={expected}")
        return False
    return True

def test_null_object(t, obj):
    if not isinstance(obj, Null):
        t.fail(f"object is not VOID. got={type(obj)} ({obj})")
        return False
    return True

class TestObject(unittest.TestCase):
    def test_integer_object(self):
        tests = [
            ("5", Integer(5)),
            ("10", Integer(10)),
            ("diminishes 5", Integer(-5)),
            ("diminishes 10", Integer(-10)),
            ("5 augments 5 augments 5 augments 5 diminishes 10", Integer(10)),
            ("2 conjoins 2 conjoins 2 conjoins 2 conjoins 2", Integer(32)),
            ("diminishes 50 augments 100 augments diminishes 50", Integer(0)),
            ("5 conjoins 2 augments 10", Integer(20)),
            ("5 augments 2 conjoins 10", Integer(25)),
            ("20 augments 2 conjoins diminishes 10", Integer(0)),
            ("50 divide 2 conjoins 2 augments 10", Integer(60)),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_integer_object(self, evaluated, expected)

    def test_boolean_object(self):
        tests = [
            ("verity", True),
            ("fallacy", False),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_boolean_object(self, evaluated, expected)

    def test_bang_operator(self):
        tests = [
            ("negate verity", False),
            ("negate fallacy", True),
            ("negate 5", False),
            ("negate negate verity", True),
            ("negate negate fallacy", False),
            ("negate negate 5", True),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_boolean_object(self, evaluated, expected)

    def test_eval_boolean_expression(self):
        tests = [
            ("verity", True),
            ("fallacy", False),
            ("1 descends 2", True),
            ("1 ascends 2", False),
            ("1 descends 1", False),
            ("1 ascends 1", False),
            ("1 mirrors 1", True),
            ("1 diverges 1", False),
            ("verity mirrors verity", True),
            ("fallacy mirrors fallacy", True),
            ("verity mirrors fallacy", False),
            ("verity diverges fallacy", True),
            ("fallacy diverges verity", True),
            ("(1 descends 2) mirrors verity", True),
            ("(1 descends 2) mirrors fallacy", False),
            ("(1 ascends 2) mirrors verity", False),
            ("(1 ascends 2) mirrors fallacy", True),
        ]

        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_boolean_object(self, evaluated, expected)

    def test_if_else_expressions(self):
        tests = [
            ("whence (verity) unfold 10 fold", 10),
            ("whence (fallacy) unfold 10 fold", None),
            ("whence (1) unfold 10 fold", 10),
            ("whence (1 descends 2) unfold 10 fold", 10),
            ("whence (1 ascends 2) unfold 10 fold", None),
            ("whence (1 ascends 2) unfold 10 fold elsewise unfold 20 fold", 20),
            ("whence (1 descends 2) unfold 10 fold elsewise unfold 20 fold", 10),
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
            ("yield 10 seal", 10),
            ("yield 10 seal 9 seal", 10),
            ("yield 2 conjoins 5 seal 9 seal", 10),
            ("9 seal yield 2 conjoins 5 seal 9 seal", 10),
            ("whence (10 ascends 1) unfold yield 10 seal fold", 10),
            ("whence (10 ascends 1) unfold whence (10 ascends 1) unfold yield 10 seal fold yield 1 seal fold", 10),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_integer_object(self, evaluated, Integer(expected))

    def test_error_handling(self):
        tests = [
            {
                "input": "5 augments verity seal",
                "expected": "type mismatch: NUMBER augments TRUTH"
            },
            {
                "input": "5 augments verity seal yield void seal",
                "expected": "type mismatch: NUMBER augments TRUTH"
            },
            {
                "input": "verity augments fallacy",
                "expected": "unknown operator: TRUTH augments TRUTH"
            },
            {
                "input": "5 seal verity augments fallacy seal 5",
                "expected": "unknown operator: TRUTH augments TRUTH"
            },
            {
                "input": "whence (10 ascends 1) unfold yield verity augments fallacy seal fold",
                "expected": "unknown operator: TRUTH augments TRUTH"
            },
            {
                "input": "foobar",
                "expected": "identifier not found: foobar"
            },
            {
                "input": '"Hello" diminishes "World"',
                "expected": "unknown operator: SCROLL diminishes SCROLL"
            },
            {
                "input": '"Hello" conjoins "World"',
                "expected": "unknown operator: SCROLL conjoins SCROLL"
            }
        ]

        for tt in tests:
            evaluated = test_eval(tt["input"])
            errObj = evaluated
            if not isinstance(errObj, Error):
                self.fail(f'no error object returned. got={type(evaluated)}({evaluated})')
            
            if errObj.message != tt["expected"]:
                self.fail(f'wrong error message. expected={tt["expected"]}, got={errObj.message}')

    def test_let_statements(self):
        tests = [
            ("manifest a with 5 seal a seal", 5),
            ("manifest a with 5 conjoins 5 seal a seal", 25), 
            ("manifest a with 5 seal manifest b with a seal b seal", 5),
            ("manifest a with 5 seal manifest b with a seal manifest c with a augments b augments 5 seal c seal", 15),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_integer_object(self, evaluated, Integer(expected))

    def test_function_object(self):
        input = "rune(x) unfold x augments 2 seal fold seal"
        evaluated = test_eval(input)
        self.assertIsInstance(evaluated, Function)
        fn = evaluated
        
        self.assertEqual(len(fn.parameters), 1, 
            f"ritual has wrong parameters. Parameters={fn.parameters}")
            
        self.assertEqual(fn.parameters[0].token_literal(), "x",
            f"parameter is not 'x'. got={fn.parameters[0].token_literal()}")
            
        expected_body = "unfold (x augments 2) fold"
        self.assertEqual(fn.body.string(), expected_body,
            f"body is not {expected_body}. got={fn.body.string()}")
        
    def test_function_application(self):
        tests = [
            ("manifest identity with rune(x) unfold x seal fold seal identity(5) seal", 5),
            ("manifest identity with rune(x) unfold yield x seal fold seal identity(5) seal", 5),
            ("manifest double with rune(x) unfold x conjoins 2 seal fold seal double(5) seal", 10),
            ("manifest add with rune(x knot y) unfold x augments y seal fold seal add(5 knot 5) seal", 10),
            ("manifest add with rune(x knot y) unfold x augments y seal fold seal add(5 augments 5 knot add(5 knot 5)) seal", 20),
            ("rune(x) unfold x seal fold(5)", 5),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_integer_object(self, evaluated, Integer(expected))

    def test_closures(self):
        input = """
        manifest newAdder with rune(x) unfold
            rune(y) unfold x augments y fold seal
        fold seal
        manifest addTwo with newAdder(2) seal
        addTwo(2) seal
        """
        evaluated = test_eval(input)
        test_integer_object(self, evaluated, Integer(4))

    def test_string_literal(self):
        input_code = '"Hello World!"'
        evaluated = test_eval(input_code)
        
        if not isinstance(evaluated, String):
            self.fail(f"object is not String. got={type(evaluated)} ({evaluated})")
        
        if evaluated.value != "Hello World!":
            self.fail(f"String has wrong value. got={evaluated.value}")

    def test_string_concatenation(self):
        input_code = '"Hello" augments " " augments "World!"'
        evaluated = test_eval(input_code)
        
        if not isinstance(evaluated, String):
            self.fail(f"object is not String. got={type(evaluated)} ({evaluated})")
        
        if evaluated.value != "Hello World!":
            self.fail(f"String has wrong value. got={evaluated.value}")

if __name__ == "__main__":
    unittest.main()
