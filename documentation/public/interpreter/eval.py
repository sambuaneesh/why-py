from object import *
from ast1 import *
from environment import Environment

# Esoteric operator mappings
OPERATOR_MAP = {
    "augments": "+",
    "diminishes": "-",
    "negate": "!",
    "conjoins": "*",
    "divide": "/",
    "descends": "<",
    "ascends": ">",
    "mirrors": "==",
    "diverges": "!="
}

# instead of creating new instance every time using singletons
VERITY = Boolean(True)
FALLACY = Boolean(False)
VOID = Null()

def is_mishap(obj: Object) -> bool:
    return obj is not None and obj.type() == ERROR_OBJ

def Eval(node: Node, env: Environment) -> Object:
    if isinstance(node, Program):
        return eval_program(node, env)
    elif isinstance(node, ExpressionStatement):
        return Eval(node.expression, env)
    elif isinstance(node, IntegerLiteral):
        return Integer(node.value)
    elif isinstance(node, BooleanLiteral):
        return VERITY if node.value else FALLACY
    elif isinstance(node, StringLiteral):
        return String(node.value)
    elif isinstance(node, PrefixExpression):
        right = Eval(node.right, env)
        if is_mishap(right):
            return right
        return eval_prefix_expression(node.operator, right, env)
    elif isinstance(node, InfixExpression):
        left = Eval(node.left, env)
        if is_mishap(left):
            return left
        right = Eval(node.right, env)
        if is_mishap(right):
            return right
        return eval_infix_expression(node.operator, left, right)
    elif isinstance(node, BlockStatement):
        return eval_block_statement(node, env)
    elif isinstance(node, IfExpression):
        return eval_if_expression(node, env)
    elif isinstance(node, ReturnStatement):
        val = Eval(node.return_value, env)
        if is_mishap(val):
            return val
        return ReturnValue(val)
    elif isinstance(node, LetStatement):
        val = Eval(node.value, env)
        if is_mishap(val):
            return val
        env.set(node.name.value, val)
    elif isinstance(node, Identifier):
        return eval_identifier(node, env)
    elif isinstance(node, FunctionLiteral):
        params = node.parameters
        body = node.body
        return Function(params, body, env)
    elif isinstance(node, CallExpression):
        function = Eval(node.function, env)
        if is_mishap(function):
            return function
        args = eval_expressions(node.arguments, env)
        if len(args) == 1 and is_mishap(args[0]):
            return args[0]
        return apply_function(function, args)
    else:
        return VOID

def eval_program(program: Program, env: Environment) -> Object:
    result = None
    for statement in program.statements:
        result = Eval(statement, env)
        if isinstance(result, ReturnValue):
            return result.value
        if is_mishap(result):
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
        if is_mishap(result):
            return result
    return result

def eval_prefix_expression(operator: str, right: Object, env: Environment) -> Object:
    if operator == "negate":
        return eval_bang_operator_expression(right)
    elif operator == "diminishes":
        return eval_minus_prefix_operator_expression(right)
    return Error(f"unknown operator: {operator} {right.type()}")

def eval_bang_operator_expression(right: Object) -> Object:
    if right == VERITY:
        return FALLACY
    elif right == FALLACY:
        return VERITY
    elif right == VOID:
        return VERITY
    return FALLACY

def eval_minus_prefix_operator_expression(right: Object) -> Object:
    if right.type() != INTEGER_OBJ:
        return Error(f"unknown operator: diminishes {right.type()}")
    value = right.value
    return Integer(-value)

def eval_infix_expression(operator: str, left: Object, right: Object) -> Object:
    """Evaluate an infix expression"""
    if left.type() != right.type():
        return Error(f"type mismatch: {left.type()} {operator} {right.type()}")
    if left.type() == INTEGER_OBJ and right.type() == INTEGER_OBJ:
        return eval_integer_infix_expression(operator, left, right)
    elif left.type() == STRING_OBJ and right.type() == STRING_OBJ:
        return eval_string_infix_expression(operator, left, right)
    elif operator == "mirrors":
        return VERITY if left == right else FALLACY
    elif operator == "diverges":
        return VERITY if left != right else FALLACY
    return Error(f"unknown operator: {left.type()} {operator} {right.type()}")

def eval_string_infix_expression(operator: str, left: Object, right: Object) -> Object:
    """Evaluate a string infix expression"""
    if operator != "augments":
        return Error(f"unknown operator: {left.type()} {operator} {right.type()}")
    
    left_val = left.value
    right_val = right.value
    return String(left_val + right_val)

def eval_integer_infix_expression(operator: str, left: Integer, right: Integer) -> Object:
    left_val = left.value
    right_val = right.value
    
    # Convert esoteric operators to standard ones
    std_operator = OPERATOR_MAP.get(operator, operator)
    
    if std_operator == "+":
        return Integer(left_val + right_val)
    elif std_operator == "-":
        return Integer(left_val - right_val)
    elif std_operator == "*":
        return Integer(left_val * right_val)
    elif std_operator == "/":
        return Integer(left_val / right_val)
    elif std_operator == "==":
        return VERITY if left_val == right_val else FALLACY
    elif std_operator == "!=":
        return VERITY if left_val != right_val else FALLACY
    elif std_operator == "<":
        return VERITY if left_val < right_val else FALLACY
    elif std_operator == ">":
        return VERITY if left_val > right_val else FALLACY
    return Error(f"unknown operator: {left.type()} {operator} {right.type()}")

def eval_if_expression(node: IfExpression, env: Environment) -> Object:
    condition = Eval(node.condition, env)
    if is_mishap(condition):
        return condition
    if is_truthy(condition):
        return Eval(node.consequence, env)
    elif node.alternative:
        return Eval(node.alternative, env)
    return VOID

def is_truthy(obj: Object) -> bool:
    if obj == VERITY:
        return True
    elif obj == FALLACY:
        return False
    elif obj == VOID:
        return False
    return True

def eval_identifier(node: Identifier, env: Environment) -> Object:
    val, exists = env.get(node.value)
    if not exists:
        return Error(f"identifier not found: {node.value}")
    return val

def eval_expressions(exps: List[Expression], env: Environment) -> List[Object]:
    result = []
    for exp in exps:
        evaluated = Eval(exp, env)
        if is_mishap(evaluated):
            return [evaluated] + result
        result.append(evaluated)
    return result

def apply_function(fn: Object, args: List[Object]) -> Object:
    if isinstance(fn, Function):
        extended_env = extend_function_env(fn, args)
        evaluated = Eval(fn.body, extended_env)
        return unwrap_return_value(evaluated)
    return Error(f"not a ritual: {fn.type()}")

def extend_function_env(fn: Function, args: List[Object]) -> Environment:
    env = Environment.new_enclosed_environment(fn.env)
    for param_idx, param in enumerate(fn.parameters):
        env.set(param.value, args[param_idx])
    return env

def unwrap_return_value(obj: Object) -> Object:
    if isinstance(obj, ReturnValue):
        return obj.value
    return obj
