---
title: Abstract Syntax Tree Implementation
description: Detailed explanation of PyFly's Abstract Syntax Tree (AST) implementation
---

# Abstract Syntax Tree Implementation

The Abstract Syntax Tree (AST) is the core data structure that represents the syntactic structure of PyFly programs. It's implemented in `ast1.py` and provides a hierarchical representation of the program's syntax.

## Overview

The AST implementation consists of several key components:

1. Base node interfaces
2. Statement nodes
3. Expression nodes
4. Program root node

## Base Node Interfaces

The AST defines two main interfaces that all nodes must implement:

```python
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
        pass

class Expression(Node):
    """Base class for all expression nodes"""
    @abc.abstractmethod
    def expression_node(self):
        pass
```

## Program Node

The root node of every AST:

```python
class Program:
    def __init__(self, statements: List[Statement]):
        self.statements = statements

    def token_literal(self) -> str:
        return self.statements[0].token_literal() if self.statements else ""

    def string(self) -> str:
        return "".join(stmt.string() for stmt in self.statements)
```

## Statement Nodes

### Let Statement

Represents variable declarations:

```python
class LetStatement(Statement):
    def __init__(self, token: Token, name: Identifier, value: Optional[Expression]):
        self.token = token  # The LET token
        self.name = name
        self.value = value

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return f"{self.token_literal()} {self.name.string()} = {self.value.string()};"
```

### Return Statement

Represents return statements:

```python
class ReturnStatement(Statement):
    def __init__(self, token: Token, return_value: Optional[Expression]):
        self.token = token
        self.return_value = return_value

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return f"{self.token_literal()} {self.return_value.string()};"
```

### Expression Statement

Wraps expressions that are used as statements:

```python
class ExpressionStatement(Statement):
    def __init__(self, token: Token, expression: Optional[Expression]):
        self.token = token
        self.expression = expression

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return self.expression.string() if self.expression else ""
```

## Expression Nodes

### Identifier

Represents variable names:

```python
class Identifier(Expression):
    def __init__(self, token: Token, value: str):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return self.value
```

### Integer Literal

Represents numeric values:

```python
class IntegerLiteral(Expression):
    def __init__(self, token: Token, value: int):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return self.token.literal
```

### Boolean Literal

Represents boolean values:

```python
class Boolean(Expression):
    def __init__(self, token: Token, value: bool):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return self.token.literal
```

## Complex Expressions

### Prefix Expression

Represents unary operations:

```python
class PrefixExpression(Expression):
    def __init__(self, token: Token, operator: str, right: Expression):
        self.token = token
        self.operator = operator
        self.right = right

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return f"({self.operator}{self.right.string()})"
```

### Infix Expression

Represents binary operations:

```python
class InfixExpression(Expression):
    def __init__(self, token: Token, left: Expression, operator: str, right: Expression):
        self.token = token
        self.left = left
        self.operator = operator
        self.right = right

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return f"({self.left.string()} {self.operator} {self.right.string()})"
```

## Function-Related Nodes

### Function Literal

Represents function definitions:

```python
class FunctionLiteral(Expression):
    def __init__(self, token: Token, parameters: List[Identifier], body: BlockStatement):
        self.token = token
        self.parameters = parameters
        self.body = body

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        params = ", ".join(param.string() for param in self.parameters)
        return f"{self.token_literal()}({params}) {self.body.string()}"
```

### Call Expression

Represents function calls:

```python
class CallExpression(Expression):
    def __init__(self, token: Token, function: Expression, arguments: List[Expression]):
        self.token = token
        self.function = function
        self.arguments = arguments

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        args = ", ".join(arg.string() for arg in self.arguments)
        return f"{self.function.string()}({args})"
```

## Best Practices

The AST implementation follows these best practices:

1. Clear class hierarchy
2. Strong typing
3. Immutable node properties
4. Comprehensive string representations
5. Memory-efficient design

## Usage Example

Here's how to construct and use AST nodes:

```python
# Create a simple let statement
let_token = Token(TokenType.LET, "let")
name_token = Token(TokenType.IDENT, "x")
value_token = Token(TokenType.INT, "5")

name = Identifier(name_token, "x")
value = IntegerLiteral(value_token, 5)
let_stmt = LetStatement(let_token, name, value)

# Print the statement
print(let_stmt.string())  # Output: let x = 5;
``` 