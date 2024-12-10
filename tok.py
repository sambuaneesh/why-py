from enum import Enum, auto

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

    # bonus datatypes
    STRING = auto()

class Token:
    def __init__(self, type: TokenType, literal: str):
        self.type = type
        self.literal = literal

    def __repr__(self):
        return f"Token(type={self.type}, literal='{self.literal}')"
