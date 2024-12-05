from object import *
from ast1 import *

# instead of creating new instance every time using singletons
TRUE = Boolean(True)
FALSE = Boolean(False)
NULL = Null()

def Eval(node: Node) -> Object:
    if isinstance(node, Program):
        return eval_statements(node.statements)
    elif isinstance(node, ExpressionStatement):
        return Eval(node.expression)
    elif isinstance(node, IntegerLiteral):
        return Integer(node.value)
    elif isinstance(node, BooleanLiteral):
        return TRUE if node.value else FALSE
    else:
        return None

def eval_statements(statements: List[Statement]) -> Object:
    result = None
    for statement in statements:
        result = Eval(statement)
    return result
