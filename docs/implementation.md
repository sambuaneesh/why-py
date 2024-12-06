# WhyPY Implementation Details

## Architecture Overview

WhyPY is implemented as a tree-walking interpreter with the following components:

1. **Lexer** - Transforms source code into tokens
2. **Parser** - Builds Abstract Syntax Tree using Pratt parsing
3. **AST** - Represents program structure
4. **Evaluator** - Executes the AST
5. **Object System** - Represents values and types

## Implementation Choices

### Why Python?

WhyPY is implemented in Python for several pragmatic reasons:

1. **Automatic Memory Management**
   - Garbage collection handled automatically
   - No need for manual memory management
   - Focus on language semantics

2. **Rich Standard Library**
   - Built-in data structures
   - Testing frameworks
   - String manipulation tools

3. **Accessibility**
   - Widely understood syntax
   - Great for collaboration
   - Extensive documentation

### Why Not Lisp?

While Lisp would be a natural choice for an interpreter, we avoided it due to the "Curse of Lisp":

1. **The Curse Explained**
   - Lisp's unique syntax can be alienating
   - Steep learning curve for collaborators
   - Limited tooling compared to mainstream languages

2. **Collaboration Barriers**
   - Smaller developer community
   - Less familiar syntax
   - Fewer available resources

## Core Components

### 1. Lexer

The lexer transforms source code into a stream of tokens:

```python
class Lexer:
    def next_token(self) -> Token:
        """Returns the next token in the input."""
        self._skip_whitespace()
        
        # Token identification logic
        if self.ch == '+':
            tok = Token(TokenType.PLUS, "augments")
        # ... more token handling ...
```

### 2. Parser

WhyPY uses Vaughan Pratt parsing for elegant expression handling:

```python
class Parser:
    def parse_expression(self, precedence: int) -> Expression:
        """Parses expressions using Pratt parsing."""
        prefix = self.prefix_parse_fns.get(self.cur_token.type)
        if not prefix:
            return None
            
        left_exp = prefix()
        
        while precedence < self.peek_precedence():
            infix = self.infix_parse_fns.get(self.peek_token.type)
            if not infix:
                return left_exp
                
            self.next_token()
            left_exp = infix(left_exp)
            
        return left_exp
```

### 3. AST (Abstract Syntax Tree)

The AST represents the program's structure:

```python
class Program:
    """Root node of every AST"""
    def __init__(self):
        self.statements = []

class LetStatement:
    """Represents a variable declaration"""
    def __init__(self):
        self.token = None  # The 'manifest' token
        self.name = None   # The identifier
        self.value = None  # The expression
```

### 4. Evaluator

The evaluator executes the AST through recursive traversal:

```python
def Eval(node: Node, env: Environment) -> Object:
    """Evaluates an AST node in the given environment."""
    if isinstance(node, Program):
        return eval_program(node, env)
    elif isinstance(node, ExpressionStatement):
        return Eval(node.expression, env)
    # ... more node types ...
```

### 5. Object System

The object system represents runtime values:

```python
class Object(abc.ABC):
    @abc.abstractmethod
    def type(self) -> str:
        pass

class Integer(Object):
    def __init__(self, value: int):
        self.value = value
    
    def type(self) -> str:
        return "NUMBER"
```

## Key Features

### 1. First-Class Functions

Functions are first-class citizens:

```python
class Function(Object):
    def __init__(self, params, body, env):
        self.parameters = params
        self.body = body
        self.env = env  # Captures the creation environment
```

### 2. Closures

Proper lexical scoping through environment chains:

```python
class Environment:
    def __init__(self, outer=None):
        self.store = {}
        self.outer = outer
    
    def get(self, name: str) -> Object:
        obj = self.store.get(name)
        if obj is None and self.outer is not None:
            return self.outer.get(name)
        return obj
```

### 3. Error Handling

Comprehensive error handling throughout:

```python
class Error(Object):
    def __init__(self, message: str):
        self.message = message
    
    def type(self) -> str:
        return "MISHAP"
```

## Testing

WhyPY includes comprehensive tests:

```python
class TestEvaluator(unittest.TestCase):
    def test_integer_expression(self):
        tests = [
            ("5", 5),
            ("10", 10),
            ("5 augments 5", 10),
            ("5 diminishes 5", 0),
            ("5 conjoins 5", 25),
            ("5 divide 5", 1),
        ]
        
        for input, expected in tests:
            evaluated = self.eval_input(input)
            self.assertEqual(evaluated.value, expected)
```

## Performance Considerations

1. **Tree-Walking Interpreter**
   - Prioritizes clarity over performance
   - No compilation step
   - Direct AST execution

2. **Memory Management**
   - Relies on Python's garbage collector
   - No manual memory management
   - Potential for optimization
