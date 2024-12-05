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
    elif isinstance(node, InfixExpression):
        left = Eval(node.left)
        right = Eval(node.right)
        return eval_infix_expression(node.operator, left, right)
    elif isinstance(node, BlockStatement):
        return eval_statements(node.statements)
    elif isinstance(node, IfExpression):
        return eval_if_expression(node)
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
    elif operator == "-":
        return eval_minus_prefix_operator_expression(right)
    return NULL

def eval_bang_operator_expression(right: Object) -> Object:
    if right == TRUE:
        return FALSE
    elif right == FALSE:
        return TRUE
    return FALSE

def eval_minus_prefix_operator_expression(right: Object) -> Object:
    if right.type() != INTEGER_OBJ:
        return NULL
    value = right.value
    return Integer(-value)

def eval_infix_expression(operator: str, left: Object, right: Object) -> Object:
    if left.type() == INTEGER_OBJ and right.type() == INTEGER_OBJ:
        return eval_integer_infix_expression(operator, left, right)
    elif operator == "==":
        return TRUE if left == right else FALSE
    elif operator == "!=":
        return TRUE if left != right else FALSE
    return NULL

def eval_integer_infix_expression(operator: str, left: Integer, right: Integer) -> Object:
    left_val = left.value
    right_val = right.value
    if operator == "+":
        return Integer(left_val + right_val)
    elif operator == "-":
        return Integer(left_val - right_val)
    elif operator == "*":
        return Integer(left_val * right_val)
    elif operator == "/":
        return Integer(left_val / right_val)
    elif operator == "==":
        return TRUE if left_val == right_val else FALSE
    elif operator == "!=":
        return TRUE if left_val != right_val else FALSE
    elif operator == "<":
        return TRUE if left_val < right_val else FALSE
    elif operator == ">":
        return TRUE if left_val > right_val else FALSE
    return NULL

def eval_if_expression(node: IfExpression) -> Object:
    condition = Eval(node.condition)
    if is_truthy(condition):
        return Eval(node.consequence)
    elif node.alternative:
        return Eval(node.alternative)
    return NULL

def is_truthy(obj: Object) -> bool:
    if obj == TRUE:
        return True
    elif obj == FALSE:
        return False
    return False
