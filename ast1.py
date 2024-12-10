from typing import List, Optional
import abc
from lexer import Token, TokenType

# Esoteric syntax mappings
OPERATOR_MAP = {
    "=": "with",
    "+": "augments",
    "-": "diminishes",
    "!": "negate",
    "*": "conjoins",
    "/": "divide",
    "<": "descends",
    ">": "ascends",
    "==": "mirrors",
    "!=": "diverges",
    ",": "knot",
    ";": "seal",
    "{": "unfold",
    "}": "fold"
}

class Node(abc.ABC):
    @abc.abstractmethod
    def token_literal(self) -> str:
        """Return the literal value of the token"""
        pass

    @abc.abstractmethod
    def string(self) -> str:
        """Return a string representation of the node"""
        pass

class Statement(Node):
    """Base class for all statement nodes"""
    @abc.abstractmethod
    def statement_node(self):
        """Marker method to distinguish statement nodes"""
        pass

class Expression(Node):
    """Base class for all expression nodes"""
    @abc.abstractmethod
    def expression_node(self):
        """Marker method to distinguish expression nodes"""
        pass

class Program:
    """Represents the entire AST of a program"""
    def __init__(self, statements: List[Statement]):
        self.statements = statements

    def token_literal(self) -> str:
        """Return the token literal of the first statement, if any"""
        return self.statements[0].token_literal() if self.statements else ""

    def string(self) -> str:
        """Convert all statements to a single string"""
        return "".join(stmt.string() for stmt in self.statements)

class Identifier(Expression):
    """Represents an identifier"""
    def __init__(self, token: Token, value: str):
        self.token = token  # The IDENT token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return self.value

class BooleanLiteral(Expression):
    """Represents a boolean literal"""
    def __init__(self, token: Token, value: bool):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return "verity" if self.value else "fallacy"

class IntegerLiteral(Expression):
    """Represents an integer literal"""
    def __init__(self, token: Token, value: int):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return str(self.value)

class StringLiteral(Expression):
    """Represents a string literal"""
    def __init__(self, token: Token, value: str):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return self.token.literal

class LetStatement(Statement):
    """Represents a let statement"""
    def __init__(self, token: Token, name: Identifier, value: Optional[Expression]):
        self.token = token  # The LET token
        self.name = name
        self.value = value

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        s = f"{self.token_literal()} {self.name.string()} with "
        if self.value:
            s += self.value.string()
        s += " seal"
        return s

class ReturnStatement(Statement):
    """Represents a return statement"""
    def __init__(self, token: Token, return_value: Optional[Expression]):
        self.token = token  # The RETURN token
        self.return_value = return_value

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        s = f"yield "
        if self.return_value:
            s += self.return_value.string()
        s += " seal"
        return s

class ExpressionStatement(Statement):
    """Represents a statement that is an expression"""
    def __init__(self, token: Token, expression: Optional[Expression]):
        self.token = token  # The first token of the expression
        self.expression = expression

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return self.expression.string() if self.expression else ""

class BlockStatement(Statement):
    """Represents a block of statements enclosed in braces"""
    def __init__(self, token: Token, statements: List[Statement]):
        self.token = token  # The { token
        self.statements = statements

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return f"unfold {' '.join(stmt.string() for stmt in self.statements)} fold"

class PrefixExpression(Expression):
    """Represents a prefix expression (e.g., !true, -5)"""
    def __init__(self, token: Token, operator: str, right: Expression):
        self.token = token  # The prefix token (!, -)
        self.operator = operator
        self.right = right

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        op = OPERATOR_MAP.get(self.operator, self.operator)
        return f"({op} {self.right.string()})"

class InfixExpression(Expression):
    """Represents an infix expression (e.g., 5 + 5, a == b)"""
    def __init__(self, token: Token, left: Expression, operator: str, right: Expression):
        self.token = token  # The operator token
        self.left = left
        self.operator = operator
        self.right = right

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        op = OPERATOR_MAP.get(self.operator, self.operator)
        return f"({self.left.string()} {op} {self.right.string()})"

class IfExpression(Expression):
    """Represents an if-else expression"""
    def __init__(
        self, 
        token: Token, 
        condition: Expression, 
        consequence: BlockStatement, 
        alternative: Optional[BlockStatement] = None
    ):
        self.token = token  # The 'if' token
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        s = f"whence {self.condition.string()} {self.consequence.string()}"
        if self.alternative:
            s += f" elsewise {self.alternative.string()}"
        return s

class FunctionLiteral(Expression):
    """Represents a function literal"""
    def __init__(
        self, 
        token: Token, 
        parameters: List[Identifier], 
        body: BlockStatement
    ):
        self.token = token  # The 'fn' token
        self.parameters = parameters
        self.body = body

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        params = " knot ".join(param.string() for param in self.parameters)
        return f"rune({params}) {self.body.string()}"

class CallExpression(Expression):
    """Represents a function call"""
    def __init__(
        self, 
        token: Token, 
        function: Expression, 
        arguments: List[Expression]
    ):
        self.token = token  # The '(' token
        self.function = function
        self.arguments = arguments

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        args = " knot ".join(arg.string() for arg in self.arguments)
        return f"{self.function.string()}({args})"
    
class GroupedExpression(Expression):
    def __init__(self, token: Token, expression: Optional[Expression] = None):
        super().__init__(token)
        self.expression = expression
