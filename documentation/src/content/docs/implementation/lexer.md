---
title: Lexer Implementation
description: Deep dive into PyFly's lexical analyzer implementation
---

# Lexer Implementation

The lexer (lexical analyzer) is the first phase of the PyFly interpreter. It transforms the source code into a sequence of tokens that can be processed by the parser.

## Overview

The lexer implementation is contained in `lexer.py` and consists of three main components:

1. Token definitions
2. The Lexer class
3. Helper functions

## Token Types

PyFly defines its tokens using Python's `Enum` class:

```python
class TokenType(Enum):
    ILLEGAL = auto()
    EOF = auto()
    
    # Identifiers + literals
    IDENT = auto()
    INT = auto()
    
    # Operators
    ASSIGN = auto()
    PLUS = auto()
    MINUS = auto()
    BANG = auto()
    ASTERISK = auto()
    SLASH = auto()
    
    # Comparison operators
    LT = auto()
    GT = auto()
    EQ = auto()
    NOT_EQ = auto()
    
    # Delimiters
    COMMA = auto()
    SEMICOLON = auto()
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    
    # Keywords
    FUNCTION = auto()
    LET = auto()
    TRUE = auto()
    FALSE = auto()
    IF = auto()
    ELSE = auto()
    RETURN = auto()
```

## Token Structure

Each token is represented by the `Token` class:

```python
class Token:
    def __init__(self, type: TokenType, literal: str):
        self.type = type
        self.literal = literal
```

## Lexer Class

The `Lexer` class is responsible for converting source code into tokens. Here are its key methods:

### Initialization

```python
def __init__(self, input: str):
    self.input = input
    self.position = 0      # current position
    self.read_position = 0 # next position
    self.ch = None        # current character
    self.read_char()      # initialize first character
```

### Reading Characters

```python
def read_char(self):
    """Read the next character in the input"""
    if self.read_position >= len(self.input):
        self.ch = None
    else:
        self.ch = self.input[self.read_position]
    self.position = self.read_position
    self.read_position += 1
```

### Token Generation

The main method `next_token()` generates tokens by:

1. Skipping whitespace
2. Identifying token type based on current character
3. Building multi-character tokens (identifiers, numbers)
4. Handling special cases (operators, keywords)

## Keywords

Keywords are handled using a dictionary lookup:

```python
KEYWORDS = {
    'fn': TokenType.FUNCTION,
    'let': TokenType.LET,
    'true': TokenType.TRUE,
    'false': TokenType.FALSE,
    'if': TokenType.IF,
    'else': TokenType.ELSE,
    'return': TokenType.RETURN
}
```

## Helper Functions

### Identifier Recognition

```python
def _is_letter(ch: str) -> bool:
    """Check if character is a letter or underscore"""
    return ch is not None and (
        ('a' <= ch <= 'z') or 
        ('A' <= ch <= 'Z') or 
        ch == '_'
    )
```

### Number Recognition

```python
def _is_digit(ch: str) -> bool:
    """Check if character is a digit"""
    return ch is not None and '0' <= ch <= '9'
```

## Testing

The lexer is thoroughly tested in `lexer_test.py`. The tests cover:

1. Basic token recognition
2. Keyword identification
3. Operator handling
4. Multi-character token building
5. Error cases

## Example Usage

Here's how to use the lexer:

```python
# Create a lexer instance
input_code = "let x = 5;"
lexer = Lexer(input_code)

# Get tokens one by one
while True:
    token = lexer.next_token()
    print(token)
    if token.type == TokenType.EOF:
        break
```

## Implementation Details

### Whitespace Handling

```python
def skip_whitespace(self):
    """Skip over whitespace characters"""
    while self.ch in [' ', '\t', '\n', '\r']:
        self.read_char()
```

### Peek Character

```python
def peek_char(self) -> str:
    """Look at next character without advancing"""
    if self.read_position >= len(self.input):
        return None
    return self.input[self.read_position]
```

## Best Practices

The lexer implementation follows these best practices:

1. Clear separation of concerns
2. Strong typing using Python type hints
3. Comprehensive error handling
4. Efficient character-by-character processing
5. Minimal memory footprint
6. Extensive test coverage

## Performance Considerations

The lexer is designed to be efficient by:

1. Using single-pass tokenization
2. Minimizing string allocations
3. Using efficient character comparisons
4. Avoiding unnecessary buffer copies

## Error Handling

The lexer handles errors by:

1. Returning ILLEGAL tokens for invalid characters
2. Maintaining context for error reporting
3. Providing clear error messages
4. Continuing lexical analysis after errors 