from object import Object, Integer
from ast1 import *

def Eval(node: Node) -> Object:
    if isinstance(node, Program):
        return eval_statements(node.statements)
    elif isinstance(node, ExpressionStatement):
        return Eval(node.expression)
    elif isinstance(node, IntegerLiteral):
        return Integer(node.value)
    else:
        return None

def eval_statements(statements: List[Statement]) -> Object:
    result = None
    for statement in statements:
        result = Eval(statement)
    return result
