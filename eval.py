from object import *
from ast1 import *
from environment import Environment

# instead of creating new instance every time using singletons
TRUE = Boolean(True)
FALSE = Boolean(False)
NULL = Null()

def is_error(obj: Object) -> bool:
    return obj is not None and obj.type() == ERROR_OBJ

def Eval(node: Node, env: Environment) -> Object:
    if isinstance(node, Program):
        return eval_program(node, env)
    elif isinstance(node, ExpressionStatement):
        return Eval(node.expression, env)
    elif isinstance(node, IntegerLiteral):
        return Integer(node.value)
    elif isinstance(node, BooleanLiteral):
        return TRUE if node.value else FALSE
    elif isinstance(node, PrefixExpression):
        right = Eval(node.right, env)
        if is_error(right):
            return right
        return eval_prefix_expression(node.operator, right, env)
    elif isinstance(node, InfixExpression):
        left = Eval(node.left, env)
        if is_error(left):
            return left
        right = Eval(node.right, env)
        if is_error(right):
            return right
        return eval_infix_expression(node.operator, left, right)
    elif isinstance(node, BlockStatement):
        return eval_block_statement(node, env)
    elif isinstance(node, IfExpression):
        return eval_if_expression(node, env)
    elif isinstance(node, ReturnStatement):
        val = Eval(node.return_value, env)
        if is_error(val):
            return val
        return ReturnValue(val)
    elif isinstance(node, LetStatement):
        val = Eval(node.value, env)
        if is_error(val):
            return val
        env.set(node.name.value, val)
    elif isinstance(node, Identifier):
        return eval_identifier(node, env)
    else:
        return NULL

def eval_program(program: Program, env: Environment) -> Object:
    result = None
    for statement in program.statements:
        result = Eval(statement, env)
        if isinstance(result, ReturnValue):
            return result.value
        if is_error(result):
            return result
    return result


def eval_block_statement(block: BlockStatement, env: Environment) -> Object:
    result = None
    for statement in block.statements:
        result = Eval(statement, env)
        if result is not None and (result.type() == RETURN_VALUE_OBJ or result.type() == ERROR_OBJ):
            return result
    return result

def eval_statements(statements: List[Statement], env: Environment) -> Object:
    result = None
    for statement in statements:
        result = Eval(statement, env)
        if isinstance(result, ReturnValue):
            return result.value
        if is_error(result):
            return result
    return result

def eval_prefix_expression(operator: str, right: Object, env: Environment) -> Object:
    if operator == "!":
        return eval_bang_operator_expression(right)
    elif operator == "-":
        return eval_minus_prefix_operator_expression(right)
    return Error(f"unknown operator: {operator}{right.type()}")

def eval_bang_operator_expression(right: Object) -> Object:
    if right == TRUE:
        return FALSE
    elif right == FALSE:
        return TRUE
    elif right == NULL:
        return TRUE
    return FALSE

def eval_minus_prefix_operator_expression(right: Object) -> Object:
    if right.type() != INTEGER_OBJ:
        return Error(f"unknown operator: -{right.type()}")
    value = right.value
    return Integer(-value)

def eval_infix_expression(operator: str, left: Object, right: Object) -> Object:
    if left.type() != right.type():
        return Error(f"type mismatch: {left.type()} {operator} {right.type()}")
    if left.type() == INTEGER_OBJ and right.type() == INTEGER_OBJ:
        return eval_integer_infix_expression(operator, left, right)
    elif operator == "==":
        return TRUE if left == right else FALSE
    elif operator == "!=":
        return TRUE if left != right else FALSE
    return Error(f"unknown operator: {left.type()} {operator} {right.type()}")

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
    return Error(f"unknown operator: {left.type()} {operator} {right.type()}")

def eval_if_expression(node: IfExpression, env: Environment) -> Object:
    condition = Eval(node.condition, env)
    if is_error(condition):
        return condition
    if is_truthy(condition):
        return Eval(node.consequence, env)
    elif node.alternative:
        return Eval(node.alternative, env)
    return NULL

def is_truthy(obj: Object) -> bool:
    if obj == TRUE:
        return True
    elif obj == FALSE:
        return False
    elif obj == NULL:
        return False
    return True

def eval_identifier(node: Identifier, env: Environment) -> Object:
    val, exists = env.get(node.value)
    if not exists:
        return Error(f"identifier not found: {node.value}")
    return val
