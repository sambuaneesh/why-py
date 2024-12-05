from object import Integer
import unittest
from lexer import Lexer
from parser import Parser
from eval import Eval

def test_eval(input):
    l = Lexer(input)
    p = Parser(l)
    program = p.parse_program()
    return Eval(program)

def test_integer_object(t, obj, expected):
    if not isinstance(obj, Integer):
        t.fail(f"object is not Integer. got={type(obj)} ({obj})")
        return False
    if obj.value != expected.value:
        t.fail(f"object has wrong value. got={obj.value}, want={expected.value}")
        return False
    return True

class TestObject(unittest.TestCase):
    def test_integer_object(self):
        tests = [
            ("5", Integer(5)),
            ("10", Integer(10)),
        ]
        for (input, expected) in tests:
            with self.subTest(input=input):
                evaluated = test_eval(input)
                test_integer_object(self, evaluated, expected)

if __name__ == "__main__":
    unittest.main()
