---
title: Parser Implementation
description: Detailed explanation of the custom interpreter's parser implementation using recursive descent and Pratt parsing
---

# Parser Implementation

The parser is the second phase of our interpreter. It takes the tokens produced by the lexer and constructs an Abstract Syntax Tree (AST) that represents the program's structure.

## Overview

Our parser is implemented using a combination of:

1. Recursive Descent Parsing for statements
2. Pratt Parsing for expressions
3. Operator precedence parsing for mathematical operations

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

# Precedence mapping
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
        
        # Prefix and infix parse function registries
        self.prefix_parse_fns: Dict[TokenType, Callable[[], Optional[Expression]]] = {}
        self.infix_parse_fns: Dict[TokenType, Callable[[Expression], Optional[Expression]]] = {}
        
        # Register parsing functions
        self._register_prefix_fns()
        self._register_infix_fns()
        
        # Initialize tokens
        self.next_token()
        self.next_token()
```

### Parse Function Registration

```python
def _register_prefix_fns(self):
    """Register prefix parse functions"""
    self.prefix_parse_fns = {
        TokenType.IDENT: self.parse_identifier,
        TokenType.INT: self.parse_integer_literal,
        TokenType.BANG: self.parse_prefix_expression,
        TokenType.MINUS: self.parse_prefix_expression,
        TokenType.TRUE: self.parse_boolean,
        TokenType.FALSE: self.parse_boolean,
        TokenType.LPAREN: self.parse_grouped_expression,
        TokenType.IF: self.parse_if_expression,
        TokenType.FUNCTION: self.parse_function_literal,
    }

def _register_infix_fns(self):
    """Register infix parse functions"""
    self.infix_parse_fns = {
        TokenType.PLUS: self.parse_infix_expression,
        TokenType.MINUS: self.parse_infix_expression,
        TokenType.SLASH: self.parse_infix_expression,
        TokenType.ASTERISK: self.parse_infix_expression,
        TokenType.EQ: self.parse_infix_expression,
        TokenType.NOT_EQ: self.parse_infix_expression,
        TokenType.LT: self.parse_infix_expression,
        TokenType.GT: self.parse_infix_expression,
        TokenType.LPAREN: self.parse_call_expression,
    }
```

## Program Parsing

The main parsing function that processes the entire program:

```python
def parse_program(self) -> Program:
    """Parse the entire program, collecting statements"""
    program = Program(statements=[])

    while not self.cur_token_is(TokenType.EOF):
        stmt = self.parse_statement()
        if stmt:
            program.statements.append(stmt)
        self.next_token()

    return program
```

## Statement Parsing

The parser handles different types of statements:

### Let Statements

```python
def parse_let_statement(self) -> Optional[LetStatement]:
    """Parse a let statement"""
    stmt = LetStatement(
        token=self.cur_token,
        name=None,
        value=None
    )

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
    """Parse a return statement"""
    stmt = ReturnStatement(
        token=self.cur_token,
        return_value=None
    )

    self.next_token()
    stmt.return_value = self.parse_expression(Precedence.LOWEST)

    if self.peek_token_is(TokenType.SEMICOLON):
        self.next_token()

    return stmt
```

## Expression Parsing

The parser uses Pratt parsing for expressions, with specialized handlers for different types:

### Expression Parsing Core

```python
def parse_expression(self, precedence: Precedence) -> Optional[Expression]:
    """Parse an expression with given precedence"""
    # Find the prefix parse function for the current token
    prefix_fn = self.prefix_parse_fns.get(self.cur_token.type)
    if not prefix_fn:
        self.no_prefix_parse_fn_error(self.cur_token.type)
        return None

    # Parse the left expression
    left_exp = prefix_fn()

    # Continue parsing infix expressions while precedence allows
    while (not self.peek_token_is(TokenType.SEMICOLON) and 
           precedence.value < self.peek_precedence().value):
        infix_fn = self.infix_parse_fns.get(self.peek_token.type)
        if not infix_fn:
            return left_exp

        self.next_token()
        left_exp = infix_fn(left_exp)

    return left_exp
```

### Function Literals and Calls

```python
def parse_function_literal(self) -> Optional[FunctionLiteral]:
    """Parse a function literal"""
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

def parse_call_expression(self, function: Expression) -> Optional[CallExpression]:
    """Parse a function call expression"""
    exp = CallExpression(
        token=self.cur_token,
        function=function,
        arguments=[]
    )
    exp.arguments = self.parse_call_arguments()
    return exp
```

## Error Handling

The parser maintains a list of errors and provides detailed error messages:

```python
def peek_error(self, token_type: TokenType):
    """Add an error message about unexpected token type"""
    error_msg = (
        f"expected next token to be {token_type}, "
        f"got {self.peek_token.type} instead"
    )
    self.errors.append(error_msg)

def no_prefix_parse_fn_error(self, token_type: TokenType):
    """Add an error message when no prefix parse function exists"""
    error_msg = f"no prefix parse function for {token_type} found"
    self.errors.append(error_msg)
```

## Best Practices

The parser implementation follows these best practices:

1. Clear separation between statement and expression parsing
2. Type-safe function registries using Python's type hints
3. Comprehensive error handling with detailed messages
4. Efficient token handling with peek and current token tracking
5. Clean separation of parsing responsibilities
6. Memory-efficient AST construction using minimal object allocation