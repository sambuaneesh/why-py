---
title: Syntax Overview
description: Overview of our custom interpreter's syntax and language constructs
---

# Syntax Overview

Our interpreter's syntax is designed to be clean, intuitive, and familiar to developers who have experience with languages like Python, JavaScript, or Go.

## Basic Syntax

### Statements and Semicolons

Every statement in our language can end with a semicolon (optional in most cases):

```python
let x = 5;
let y = 10;
```

### Identifiers

Identifiers in our language can contain:
- Letters (a-z, A-Z)
- Numbers (0-9)
- Underscore (_)

The first character must be a letter or underscore:

```python
let validName = 5;
let _alsoValid = 10;
let valid2 = 15;
```

## Data Types

### Integer Literals

The language supports integer numbers:

```python
let x = 42;
let y = 100;
let negative = -5;
```

### Boolean Literals

Boolean values are represented by `true` and `false`:

```python
let isTrue = true;
let isFalse = false;
```

## Expressions

### Arithmetic Expressions

The language supports standard arithmetic operations:

```python
let a = 5 + 10;    // Addition
let b = 20 - 5;    // Subtraction
let c = 4 * 3;     // Multiplication
let d = 15 / 3;    // Division
```

### Comparison Expressions

Comparison operators return boolean values:

```python
let isEqual = 5 == 5;      // true
let notEqual = 5 != 3;     // true
let lessThan = 5 < 10;     // true
let greaterThan = 10 > 5;  // true
```

### Prefix Expressions

The language supports prefix operators:

```python
let negation = !true;      // false
let negative = -5;         // negative number
```

## Variable Declarations

Variables are declared using the `let` keyword:

```python
let name = 42;             // integer
let isActive = true;       // boolean
let add = fn(x, y) { };    // function
```

## Functions

### Function Declarations

Functions are first-class citizens and are declared using the `fn` keyword:

```python
let add = fn(x, y) {
    return x + y;
};

let multiply = fn(x, y) {
    return x * y;
};
```

### Function Calls

Functions are called using parentheses:

```python
let result = add(5, 10);
let doubled = multiply(2, result);
```

## Control Flow

### If-Else Expressions

Conditional execution uses if-else expressions:

```python
let max = fn(x, y) {
    if (x > y) {
        return x;
    } else {
        return y;
    }
};
```

Note that if-else constructs are expressions, meaning they return a value.

### Block Statements

Code blocks can contain multiple statements and return the value of the last expression:

```python
let result = {
    let x = 5;
    let y = 10;
    x + y;  // returns 15
};
```

## Best Practices

1. Use descriptive variable and function names
2. Keep functions small and focused
3. Use proper indentation for readability
4. Break complex expressions into simpler ones
5. Use meaningful variable names that indicate their purpose

## Examples

### Function Composition

```python
let addTwo = fn(x) { return x + 2; };
let multiplyByThree = fn(x) { return x * 3; };

let composed = fn(x) {
    return multiplyByThree(addTwo(x));
};
```

### Conditional Logic

```python
let isEven = fn(x) {
    if (x % 2 == 0) {
        return true;
    } else {
        return false;
    }
};
``` 