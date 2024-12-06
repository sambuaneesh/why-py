---
title: Syntax Overview
description: Overview of PyFly's syntax and language constructs
---

# Syntax Overview

PyFly's syntax is designed to be clean, intuitive, and familiar to developers who have experience with languages like Python, JavaScript, or Go.

## Basic Syntax

### Statements and Semicolons

Every statement in PyFly ends with a semicolon:

```python
let x = 5;
let y = 10;
```

### Comments

PyFly currently supports single-line comments:

```python
// This is a comment
let x = 5;  // This is an end-of-line comment
```

### Identifiers

Identifiers in PyFly can contain:
- Letters (a-z, A-Z)
- Numbers (0-9)
- Underscore (_)

The first character must be a letter or underscore:

```python
let validName = 5;
let _alsoValid = 10;
let valid2 = 15;
```

## Expressions

### Arithmetic Expressions

PyFly supports standard arithmetic operations:

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

### Logical Expressions

PyFly supports basic logical operations:

```python
let not = !true;           // false
let comparison = 5 < 10;   // true
```

## Code Blocks

Code blocks in PyFly are enclosed in curly braces:

```python
if (x > 5) {
    return true;
} else {
    return false;
}
```

## Function Declarations

Functions are declared using the `fn` keyword:

```python
let add = fn(x, y) {
    return x + y;
};
```

## Variable Declarations

Variables are declared using the `let` keyword:

```python
let name = "PyFly";
let age = 25;
let isActive = true;
```

## Control Flow

### If-Else Statements

Conditional execution uses if-else statements:

```python
if (condition) {
    // code to execute if condition is true
} else {
    // code to execute if condition is false
}
```

## Best Practices

1. Use consistent indentation (recommended: 4 spaces)
2. End all statements with semicolons
3. Use descriptive variable and function names
4. Add comments to explain complex logic
5. Keep functions small and focused

## Common Patterns

### Function Composition

```python
let compose = fn(f, g) {
    return fn(x) {
        return f(g(x));
    };
};
```

### Higher-Order Functions

```python
let map = fn(arr, f) {
    let iter = fn(arr, accumulated) {
        if (len(arr) == 0) {
            return accumulated;
        } else {
            return iter(rest(arr), push(accumulated, f(first(arr))));
        }
    };
    return iter(arr, []);
};
``` 