---
title: Lexer Implementation
description: Deep dive into the custom interpreter's lexical analyzer implementation
---

# Lexer Implementation

The lexer (lexical analyzer) is the first phase of our interpreter. It transforms the source code into a sequence of tokens that can be processed by the parser.

## Overview

The lexer implementation is contained in `lexer.py` and consists of three main components:

1. Token handling
2. The Lexer class
3. Helper functions

## Token Handling

The lexer uses a separate `tok.py` module for token definitions and works with a predefined set of keywords:

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

def lookup_ident(literal: str) -> TokenType:
    """Check if the literal is a keyword, otherwise return IDENT"""
    return KEYWORDS.get(literal, TokenType.IDENT)
```

## Lexer Class

The `Lexer` class is responsible for converting source code into tokens. Here are its key components:

### Initialization

```python
def __init__(self, input: str):
    self.input = input
    self.position = 0      # current position in input
    self.read_position = 0 # current reading position in input
    self.ch = None        # current char under examination
    self.read_char()
```

### Character Reading

```python
def read_char(self):
    """Read the next character in the input"""
    if self.read_position >= len(self.input):
        self.ch = None
    else:
        self.ch = self.input[self.read_position]
    self.position = self.read_position
    self.read_position += 1

def peek_char(self) -> str:
    """Look at the next character without advancing"""
    if self.read_position >= len(self.input):
        return None
    return self.input[self.read_position]
```

### Token Generation

The main method `next_token()` handles token generation with special cases for:

1. Single character tokens (operators, delimiters)
2. Two-character tokens (==, !=)
3. Identifiers and keywords
4. Integer literals

```python
def next_token(self) -> Token:
    """Determine and return the next token"""
    self.skip_whitespace()

    if self.ch is None:
        return Token(TokenType.EOF, "")

    # Token handling using a mapping for single character tokens
    token_map = {
        '=': self._handle_equal,
        '+': lambda: Token(TokenType.PLUS, self.ch),
        '-': lambda: Token(TokenType.MINUS, self.ch),
        '!': self._handle_bang,
        '/': lambda: Token(TokenType.SLASH, self.ch),
        '*': lambda: Token(TokenType.ASTERISK, self.ch),
        '<': lambda: Token(TokenType.LT, self.ch),
        '>': lambda: Token(TokenType.GT, self.ch),
        ';': lambda: Token(TokenType.SEMICOLON, self.ch),
        ',': lambda: Token(TokenType.COMMA, self.ch),
        '{': lambda: Token(TokenType.LBRACE, self.ch),
        '}': lambda: Token(TokenType.RBRACE, self.ch),
        '(': lambda: Token(TokenType.LPAREN, self.ch),
        ')': lambda: Token(TokenType.RPAREN, self.ch)
    }
```

### Helper Methods

The lexer includes several helper methods for specific token types:

```python
def _handle_equal(self) -> Token:
    """Handle both single '=' and '==' tokens"""
    if self.peek_char() == '=':
        ch = self.ch
        self.read_char()
        literal = ch + self.ch
        return Token(TokenType.EQ, literal)
    return Token(TokenType.ASSIGN, self.ch)

def _handle_bang(self) -> Token:
    """Handle both single '!' and '!=' tokens"""
    if self.peek_char() == '=':
        ch = self.ch
        self.read_char()
        literal = ch + self.ch
        return Token(TokenType.NOT_EQ, literal)
    return Token(TokenType.BANG, self.ch)

@staticmethod
def _is_letter(ch: str) -> bool:
    """Check if the character is a valid letter"""
    return ch is not None and (
        ('a' <= ch <= 'z') or 
        ('A' <= ch <= 'Z') or 
        ch == '_'
    )

@staticmethod
def _is_digit(ch: str) -> bool:
    """Check if the character is a digit"""
    return ch is not None and '0' <= ch <= '9'
```

## Implementation Details

### Whitespace Handling

```python
def skip_whitespace(self):
    """Skip over whitespace characters"""
    while self.ch in [' ', '\t', '\n', '\r']:
        self.read_char()
```

### Identifier and Number Reading

```python
def read_identifier(self) -> str:
    """Read and return a complete identifier"""
    position = self.position
    while self._is_letter(self.ch):
        self.read_char()
    return self.input[position:self.position]

def read_number(self) -> str:
    """Read and return a complete number"""
    position = self.position
    while self._is_digit(self.ch):
        self.read_char()
    return self.input[position:self.position]
```

## Best Practices

The lexer implementation follows these best practices:

1. Clear separation of concerns with token handling in a separate module
2. Efficient character-by-character processing
3. Clean handling of two-character tokens
4. Strong typing using Python type hints
5. Comprehensive error handling with ILLEGAL tokens
6. Memory-efficient string slicing for identifiers and numbers

## Example Usage

```python
def main():
    # Test the lexer
    input_code = '''
    let add = fn(x, y) { 
        return x + y; 
    }; 
    add(5, 10);
    '''
    lexer = Lexer(input_code)
    
    while True:
        token = lexer.next_token()
        print(token)
        if token.type == TokenType.EOF:
            break
```