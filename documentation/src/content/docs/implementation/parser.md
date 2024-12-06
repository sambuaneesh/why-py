---
title: Parser Implementation
description: Understanding the mystical art of parsing in WhyPY
---

# Parser Implementation

## The Art of Vaughan Pratt Parsing

WhyPY employs the elegant Vaughan Pratt parsing technique, a top-down operator precedence parsing method that brings clarity to expression parsing. This approach allows us to handle complex expressions with proper precedence while maintaining the mystical nature of our syntax.

### Why Pratt Parsing?

Pratt parsing excels at handling:
- Prefix operations (`negate`, `diminishes`)
- Infix operations (`augments`, `conjoins`, `divide`)
- Operator precedence in a clean, extensible way
- Complex nested expressions

## Prefix Operations

WhyPY currently supports prefix operations as part of its mystical syntax:

```python
manifest x with negate verity seal        // Negation
manifest y with diminishes 42 seal        // Numeric negation
```

Note: Postfix operations are not yet supported in the current incarnation of WhyPY, as they would disturb the flow of mystical energy from left to right.

## Error Handling

The parser implements comprehensive error handling to guide practitioners through their mystical journey:

### Error Types

```python
manifest x with 5 augments seal  // MISHAP: Expected expression after 'augments'
manifest with 42 seal           // MISHAP: Expected identifier after 'manifest'
```

### Error Recovery

The parser employs sophisticated error recovery mechanisms to:
- Provide meaningful error messages
- Continue parsing after encountering errors
- Maintain the mystical state of the parse tree

Example error messages:
```python
MISHAP: Unexpected token 'seal' during ritual invocation
MISHAP: Expected 'fold' to close ritual body
MISHAP: Cannot bind truth value to numeric operation
```

## Expression Parsing

The parser handles various expression types:

### Prefix Expressions
```python
negate verity
diminishes 42
```

### Infix Expressions
```python
5 augments 3
x conjoins y
truth mirrors fallacy
```

### Grouped Expressions
```python
(5 augments 3) conjoins 2
```

## Implementation Details

The parser is implemented using Python, chosen for its:
- Automatic memory management through garbage collection
- Clear and readable syntax for implementing parsing logic
- Rich standard library support

### Why Not Lisp?

While Lisp would seem a natural choice for an interpreter (given its powerful metaprogramming capabilities), we chose not to use it due to the "Curse of Lisp":
- The Curse of Lisp refers to Lisp's unique syntax and concepts that can create a barrier for collaboration
- Using Python makes the codebase more accessible to contributors
- Python's ecosystem provides better tooling for our mystical purposes

## Code Structure

The parser is organized into several mystical components:

```python
class Parser:
    def parse_program(self) -> Program:
        """Parse the entire mystical program"""
        
    def parse_expression(self, precedence: int) -> Optional[Expression]:
        """Parse expressions with proper precedence"""
        
    def register_prefix(self, token_type: TokenType, fn: PrefixParseFn):
        """Register prefix parsing functions"""
        
    def register_infix(self, token_type: TokenType, fn: InfixParseFn):
        """Register infix parsing functions"""
```

## Error Examples

Here are some common parsing mishaps and their mystical meanings:

```python
// Missing seal
manifest x with 5
MISHAP: Expected 'seal' to contain the mystical energy

// Invalid ritual declaration
rune(x knot) unfold
MISHAP: Expected parameter name after 'knot'

// Unmatched unfold/fold
whence (verity) unfold
    yield 42 seal
MISHAP: Missing 'fold' to close the mystical block
```