---
title: Abstract Syntax Tree Implementation
description: Detailed explanation of the custom interpreter's Abstract Syntax Tree (AST) implementation
---

# Abstract Syntax Tree Implementation

The Abstract Syntax Tree (AST) is the core data structure that represents the syntactic structure of our interpreter's programs. It's implemented in `ast1.py` and provides a hierarchical representation of the program's syntax.

## Overview

The AST implementation consists of several key components:

1. Base node interfaces
2. Program root node
3. Statement nodes
4. Expression nodes
5. Function and control flow nodes

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

The root node that contains all statements:

```python
class Program:
    def __init__(self, statements: List[Statement]):
        self.statements = statements

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        return ""

    def string(self) -> str:
        return "".join(stmt.string() for stmt in self.statements)
```

## Statement Nodes

### Let Statement

Represents variable declarations:

```python
class LetStatement(Statement):
    def __init__(self, token: Token, name: Optional[Identifier], value: Optional[Expression]):
        self.token = token  # The 'let' token
        self.name = name    # The identifier being bound
        self.value = value  # The value expression

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        out = f"{self.token_literal()} {self.name.string()} = "
        if self.value:
            out += self.value.string()
        out += ";"
        return out
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
        out = self.token_literal()
        if self.return_value:
            out += f" {self.return_value.string()}"
        out += ";"
        return out
```

### Expression Statement

Wraps expressions that can be used as statements:

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
        if self.expression:
            return self.expression.string()
        return ""
```

## Expression Nodes

### Identifier

Represents variable names and references:

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

### Literals

Various literal types supported by the interpreter:

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

class BooleanLiteral(Expression):
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

### Operator Expressions

#### Prefix Expression

Represents unary operations:

```python
class PrefixExpression(Expression):
    def __init__(self, token: Token, operator: str, right: Optional[Expression]):
        self.token = token      # The prefix token (!, -)
        self.operator = operator
        self.right = right

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return f"({self.operator}{self.right.string()})"
```

#### Infix Expression

Represents binary operations:

```python
class InfixExpression(Expression):
    def __init__(self, token: Token, left: Expression, operator: str, right: Expression):
        self.token = token      # The operator token
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

### Function Definition and Calls

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

class CallExpression(Expression):
    def __init__(self, token: Token, function: Expression, arguments: List[Expression]):
        self.token = token      # The '(' token
        self.function = function # The identifier or function literal
        self.arguments = arguments

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        args = ", ".join(arg.string() for arg in self.arguments)
        return f"{self.function.string()}({args})"
```

## Block Statement

Represents a sequence of statements:

```python
class BlockStatement(Statement):
    def __init__(self, token: Token, statements: List[Statement]):
        self.token = token
        self.statements = statements

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        return "".join(stmt.string() for stmt in self.statements)
```

## Control Flow and Functions

### If Expression

Represents conditional expressions:

```python
class IfExpression(Expression):
    def __init__(self, token: Token, condition: Expression, 
                 consequence: BlockStatement, alternative: Optional[BlockStatement]):
        self.token = token
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def string(self) -> str:
        out = f"if{self.condition.string()} {self.consequence.string()}"
        if self.alternative:
            out += f"else {self.alternative.string()}"
        return out
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