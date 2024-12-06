---
title: Introduction to PyFly
description: A comprehensive guide to PyFly - a custom programming language interpreter written in Python
---

# Welcome to PyFly

PyFly is a custom programming language interpreter written in Python that implements a simple yet powerful programming language. It features a clean syntax inspired by modern programming languages while maintaining simplicity and ease of use.

## Features

- **Clean Syntax**: Simple and intuitive syntax that's easy to learn
- **Static Typing**: Basic type system with integers, booleans, and functions
- **First-class Functions**: Functions are first-class citizens
- **Control Flow**: Support for if-else statements and basic control structures
- **Modern Parser**: Recursive descent parser with Pratt parsing for expressions

## Architecture

PyFly is built with a modular architecture consisting of three main components:

1. **Lexer**: Transforms source code into tokens
2. **Parser**: Converts tokens into an Abstract Syntax Tree (AST)
3. **AST**: Represents the program structure in memory

## Example

Here's a simple example of PyFly code:

```python
let add = fn(x, y) {
    return x + y;
};

let result = add(5, 10);
```

## Project Status

PyFly is currently under active development. The core features are implemented and working, including:

- Lexical analysis
- Parsing
- Basic expression evaluation
- Function definitions
- Control flow statements

## Getting Started

To get started with PyFly, check out the [Installation](/getting-started/installation/) guide and then move on to the [Quick Start](/getting-started/quick-start/) tutorial. 