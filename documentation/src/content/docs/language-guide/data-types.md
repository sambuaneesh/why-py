---
title: Data Types
description: Overview of our interpreter's data types and object system
---

# Data Types

Our interpreter implements a simple but effective object system with basic data types common in most programming languages.

## Basic Types

### Integer

Integers are whole numbers:

```python
let x = 42;
let y = -17;
let z = 0;
```

Operations on integers:
- Addition: `5 + 3`
- Subtraction: `10 - 4`
- Multiplication: `6 * 7`
- Division: `15 / 3`
- Comparison: `5 < 10`, `7 > 3`, `5 == 5`, `6 != 4`

### Boolean

Boolean values can be either `true` or `false`:

```python
let isTrue = true;
let isFalse = false;
let result = 5 > 3;  // evaluates to true
```

Operations on booleans:
- Logical NOT: `!true` evaluates to `false`
- Equality: `true == true`, `false != true`

### Function

Functions are first-class values in our language:

```python
// Simple function
let add = fn(x, y) {
    return x + y;
};

// Function with multiple statements
let max = fn(x, y) {
    if (x > y) {
        return x;
    } else {
        return y;
    }
};

// Function that returns a function
let makeAdder = fn(x) {
    return fn(y) {
        return x + y;
    };
};
```

## Object System

The interpreter uses a simple object system defined in `object.py`:

### Integer Objects

```python
class Integer:
    def __init__(self, value: int):
        self.value = value

    def type(self) -> str:
        return INTEGER_OBJ
```

### Boolean Objects

```python
class Boolean:
    def __init__(self, value: bool):
        self.value = value

    def type(self) -> str:
        return BOOLEAN_OBJ
```

### Function Objects

```python
class Function:
    def __init__(self, parameters: List[Identifier], 
                 body: BlockStatement, 
                 env: Environment):
        self.parameters = parameters
        self.body = body
        self.env = env

    def type(self) -> str:
        return FUNCTION_OBJ
```

## Type System

The interpreter uses dynamic typing where types are determined at runtime:

```python
let x = 5;              // Integer
let isValid = true;     // Boolean
let add = fn(x, y) {    // Function
    return x + y;
};
```

### Type Checking

Type checking is performed at runtime during evaluation:

```python
let x = 5;
let y = 10;
x + y;    // valid: both are integers

let z = true;
x + z;    // runtime error: type mismatch
```

## Error Handling

The interpreter includes error handling for type-related issues:

```python
class Error:
    def __init__(self, message: str):
        self.message = message

    def type(self) -> str:
        return ERROR_OBJ
```

Common error cases:
- Type mismatches in operations
- Unknown operators for types
- Undefined variables
- Invalid function calls

## Best Practices

1. Use consistent types in operations
2. Handle potential type errors in your code
3. Use meaningful variable names that indicate the type
4. Keep functions type-consistent
5. Document expected types in complex functions

## Examples

### Type-Safe Operations

```python
let divide = fn(x, y) {
    if (y == 0) {
        return false;  // Error case
    }
    return x / y;
};
```

### Function Composition

```python
let compose = fn(f, g) {
    return fn(x) {
        return f(g(x));
    };
};

let addOne = fn(x) { return x + 1; };
let double = fn(x) { return x * 2; };
let addOneThenDouble = compose(double, addOne);
```