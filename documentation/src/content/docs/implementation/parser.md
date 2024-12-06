---
title: Parser Implementation
description: Detailed explanation of PyFly's parser implementation using recursive descent and Pratt parsing
---

# Parser Implementation

The parser is the second phase of the PyFly interpreter. It takes the tokens produced by the lexer and constructs an Abstract Syntax Tree (AST) that represents the program's structure.

## Overview

PyFly's parser is implemented using a combination of:

1. Recursive Descent Parsing for statements
2. Pratt Parsing for expressions

## Parser Structure

The parser is implemented in `parser.py` and consists of several key components:

### Precedence Levels

```python
class Precedence(Enum):
    LOWEST = auto()
    EQUALS = auto()      # ==
    LESSGREATER = auto() # > or <
    SUM = auto()         # +
    PRODUCT = auto()     # *
    PREFIX = auto()      # -X or !X
    CALL = auto()        # myFunction(X)
```

### Precedence Table

```python
PRECEDENCES = {
    TokenType.EQ: Precedence.EQUALS,
    TokenType.NOT_EQ: Precedence.EQUALS,
    TokenType.LT: Precedence.LESSGREATER,
    TokenType.GT: Precedence.LESSGREATER,
    TokenType.PLUS: Precedence.SUM,
    TokenType.MINUS: Precedence.SUM,
    TokenType.SLASH: Precedence.PRODUCT,
    TokenType.ASTERISK: Precedence.PRODUCT,
    TokenType.LPAREN: Precedence.CALL,
}
```

## Parser Class

The `Parser` class is the main component that handles parsing:

```python
class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.cur_token = None
        self.peek_token = None
        self.errors: List[str] = []
        
        # Register parsing functions
        self.prefix_parse_fns = {}
        self.infix_parse_fns = {}
        
        self._register_prefix_fns()
        self._register_infix_fns()
        
        # Initialize tokens
        self.next_token()
        self.next_token()
```

## Statement Parsing

The parser handles different types of statements:

### Let Statements

```python
def parse_let_statement(self) -> Optional[LetStatement]:
    stmt = LetStatement(token=self.cur_token, name=None, value=None)
    
    if not self.expect_peek(TokenType.IDENT):
        return None
        
    stmt.name = Identifier(
        token=self.cur_token,
        value=self.cur_token.literal
    )
    
    if not self.expect_peek(TokenType.ASSIGN):
        return None
        
    self.next_token()
    stmt.value = self.parse_expression(Precedence.LOWEST)
    
    if self.peek_token_is(TokenType.SEMICOLON):
        self.next_token()
        
    return stmt
```

### Return Statements

```python
def parse_return_statement(self) -> Optional[ReturnStatement]:
    stmt = ReturnStatement(token=self.cur_token, return_value=None)
    
    self.next_token()
    stmt.return_value = self.parse_expression(Precedence.LOWEST)
    
    if self.peek_token_is(TokenType.SEMICOLON):
        self.next_token()
        
    return stmt
```

## Expression Parsing

PyFly uses Pratt parsing for expressions, which associates parsing functions with token types:

### Prefix Expressions

```python
def parse_prefix_expression(self) -> Optional[Expression]:
    expression = PrefixExpression(
        token=self.cur_token,
        operator=self.cur_token.literal,
        right=None
    )
    
    self.next_token()
    expression.right = self.parse_expression(Precedence.PREFIX)
    
    return expression
```

### Infix Expressions

```python
def parse_infix_expression(self, left: Expression) -> Optional[Expression]:
    expression = InfixExpression(
        token=self.cur_token,
        operator=self.cur_token.literal,
        left=left,
        right=None
    )
    
    precedence = self.cur_precedence()
    self.next_token()
    expression.right = self.parse_expression(precedence)
    
    return expression
```

## Function Parsing

The parser handles function literals and calls:

### Function Literals

```python
def parse_function_literal(self) -> Optional[Expression]:
    lit = FunctionLiteral(
        token=self.cur_token,
        parameters=[],
        body=None
    )
    
    if not self.expect_peek(TokenType.LPAREN):
        return None
        
    lit.parameters = self.parse_function_parameters()
    
    if not self.expect_peek(TokenType.LBRACE):
        return None
        
    lit.body = self.parse_block_statement()
    
    return lit
```

## Error Handling

The parser maintains a list of errors and provides detailed error messages:

```python
def peek_error(self, token_type: TokenType):
    error_msg = (
        f"expected next token to be {token_type}, "
        f"got {self.peek_token.type} instead"
    )
    self.errors.append(error_msg)
```

## Best Practices

The parser implementation follows these best practices:

1. Clear separation between statement and expression parsing
2. Proper error handling and recovery
3. Modular design with separate parsing functions
4. Strong typing using Python type hints
5. Comprehensive test coverage

## Performance Considerations

The parser is optimized for:

1. Single-pass parsing
2. Efficient token handling
3. Minimal backtracking
4. Memory-efficient AST construction

## Testing

The parser is tested for:

1. Statement parsing
2. Expression parsing
3. Operator precedence
4. Error handling
5. Edge cases

## Example Usage

Here's how to use the parser:

```python
# Create lexer and parser
input_code = "let x = 5 + 10;"
lexer = Lexer(input_code)
parser = Parser(lexer)

# Parse the program
program = parser.parse_program()

# Check for errors
if parser.errors:
    print("Parsing errors:")
    for error in parser.errors:
        print(f"  {error}")
else:
    print(program.string())
```

## Advanced Features

The parser supports advanced features like:

1. Nested expressions
2. Function calls
3. If-else expressions
4. Grouped expressions
5. Complex operator precedence 