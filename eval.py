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
    elif isinstance(node, PrefixExpression):
        right = Eval(node.right)
        return eval_prefix_expression(node.operator, right)
    else:
        return None

def eval_statements(statements: List[Statement]) -> Object:
    result = None
    for statement in statements:
        result = Eval(statement)
    return result

def eval_prefix_expression(operator: str, right: Object) -> Object:
    if operator == "!":
        return eval_bang_operator_expression(right)
    return NULL

def eval_bang_operator_expression(right: Object) -> Object:
    if right == TRUE:
        return FALSE
    elif right == FALSE:
        return TRUE
    return FALSE
