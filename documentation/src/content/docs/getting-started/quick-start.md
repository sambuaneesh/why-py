---
title: Quick Start Guide
description: Get started with PyFly by writing your first program
---

# Quick Start Guide

This guide will help you write your first PyFly program and understand the basics of the language.

## Your First PyFly Program

Let's start with a simple program that defines a function to calculate the factorial of a number:

```python
let factorial = fn(n) {
    if (n < 2) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
};

let result = factorial(5);
```

Let's break down the key elements of this program:

1. `let` keyword declares variables
2. `fn` creates a function
3. `if/else` provides conditional execution
4. Function calls work as expected
5. Basic arithmetic operations are supported

## Basic Language Features

### 1. Variables

Variables are declared using the `let` keyword:

```python
let x = 5;
let y = 10;
let name = "PyFly";
```

### 2. Functions

Functions are first-class citizens in PyFly:

```python
let add = fn(x, y) {
    return x + y;
};

let multiply = fn(x, y) {
    return x * y;
};
```

### 3. Control Flow

PyFly supports if-else statements:

```python
let max = fn(x, y) {
    if (x > y) {
        return x;
    } else {
        return y;
    }
};
```

### 4. Operators

PyFly supports common operators:

- Arithmetic: `+`, `-`, `*`, `/`
- Comparison: `<`, `>`, `==`, `!=`
- Logical: `!` (not)

## Running Your Code

To run your PyFly code, save it in a file (e.g., `example.pf`) and use the interpreter:

```bash
python pyfly.py example.pf
```

## Next Steps

Now that you've written your first PyFly program, you can:

1. Learn more about [PyFly's syntax](/language-guide/syntax-overview/)
2. Explore [data types](/language-guide/data-types/)
3. Understand [functions in depth](/language-guide/functions/)
4. Learn about [control flow](/language-guide/control-flow/)

## Common Patterns

Here are some common patterns you'll use in PyFly:

### Higher-Order Functions

```python
let apply = fn(f, x) {
    return f(x);
};

let double = fn(x) {
    return x * 2;
};

let result = apply(double, 5);  // Returns 10
```

### Recursion

```python
let sum = fn(n) {
    if (n == 0) {
        return 0;
    }
    return n + sum(n - 1);
};
```

## Tips and Best Practices

1. Always terminate statements with semicolons
2. Use meaningful variable names
3. Break complex functions into smaller ones
4. Use proper indentation for readability
5. Comment your code when necessary

Remember that PyFly is designed to be simple and intuitive. If you're familiar with languages like Python or JavaScript, you'll find many similarities in PyFly's syntax and features. 