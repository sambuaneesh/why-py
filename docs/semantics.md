# WhyPY Semantics Guide

## Introduction

WhyPY transforms traditional programming constructs into mystical rituals through its unique esoteric semantics. This guide will help you understand the mapping between conventional programming concepts and their WhyPY equivalents.

## Token Specification

### Core Tokens

| Token Type | Esoteric Representation | Description |
|------------|------------------------|-------------|
| `ILLEGAL` | _(Unchanged)_ | Token not recognized |
| `EOF` | _(Unchanged)_ | End of input |

### Identifiers and Literals

| Token Type | Esoteric Representation | Description |
|------------|------------------------|-------------|
| `IDENT` | _(Unchanged)_ | Identifier for variables or functions |
| `INT` | _(Unchanged)_ | Integer literals |

### Operators

| Token Type | Esoteric Representation | Original Symbol | Description |
|------------|------------------------|-----------------|-------------|
| `ASSIGN` | `with` | `=` | Assignment operator |
| `PLUS` | `augments` | `+` | Addition operator |
| `MINUS` | `diminishes` | `-` | Subtraction operator |
| `BANG` | `negate` | `!` | Negation operator |
| `ASTERISK` | `conjoins` | `*` | Multiplication operator |
| `SLASH` | `divide` | `/` | Division operator |
| `LT` | `descends` | `<` | Less-than comparison |
| `GT` | `ascends` | `>` | Greater-than comparison |
| `EQ` | `mirrors` | `==` | Equality comparison |
| `NOT_EQ` | `diverges` | `!=` | Inequality comparison |

### Delimiters

| Token Type | Esoteric Representation | Original Symbol | Description |
|------------|------------------------|-----------------|-------------|
| `COMMA` | `knot` | `,` | Argument separator |
| `SEMICOLON` | `seal` | `;` | Statement terminator |
| `LPAREN` | _(Unchanged)_ | `(` | Start grouping |
| `RPAREN` | _(Unchanged)_ | `)` | End grouping |
| `LBRACE` | `unfold` | `{` | Block start |
| `RBRACE` | `fold` | `}` | Block end |

### Keywords

| Token Type | Esoteric Representation | Original Keyword | Description |
|------------|------------------------|------------------|-------------|
| `FUNCTION` | `rune` | `fn` | Function definition |
| `LET` | `manifest` | `let` | Variable declaration |
| `TRUE` | `verity` | `true` | Boolean true |
| `FALSE` | `fallacy` | `false` | Boolean false |
| `IF` | `whence` | `if` | Conditional start |
| `ELSE` | `elsewise` | `else` | Alternate condition |
| `RETURN` | `yield` | `return` | Return a value |

## Comparative Examples

### 1. Variable Declaration

Traditional Syntax:
```python
let x = 5;
let y = 10;
let sum = x + y;
```

WhyPY Syntax:
```python
manifest x with 5 seal
manifest y with 10 seal
manifest sum with x augments y seal
```

### 2. Function Definition

Traditional Syntax:
```python
let add = fn(x, y) {
    return x + y;
};
```

WhyPY Syntax:
```python
manifest add with rune(x knot y) unfold
    yield x augments y seal
fold seal
```

### 3. Conditional Statements

Traditional Syntax:
```python
let max = fn(x, y) {
    if (x > y) {
        return x;
    } else {
        return y;
    }
};
```

WhyPY Syntax:
```python
manifest max with rune(x knot y) unfold
    whence (x ascends y) unfold
        yield x seal
    fold elsewise unfold
        yield y seal
    fold
fold seal
```

### 4. Complex Arithmetic

Traditional Syntax:
```python
let result = (5 + 3) * 2 - 1;
let isPositive = result > 0;
```

WhyPY Syntax:
```python
manifest result with (5 augments 3) conjoins 2 diminishes 1 seal
manifest isPositive with result ascends 0 seal
```

### 5. Function Composition

Traditional Syntax:
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

WhyPY Syntax:
```python
manifest compose with rune(f knot g) unfold
    yield rune(x) unfold
        yield f(g(x)) seal
    fold seal
fold seal

manifest addOne with rune(x) unfold yield x augments 1 seal fold seal
manifest double with rune(x) unfold yield x conjoins 2 seal fold seal
manifest addOneThenDouble with compose(double knot addOne) seal
```

### 6. Error Handling

Traditional Syntax:
```python
let safeDivide = fn(x, y) {
    if (y == 0) {
        return null;
    }
    return x / y;
};
```

WhyPY Syntax:
```python
manifest safeDivide with rune(x knot y) unfold
    whence (y mirrors 0) unfold
        yield void seal
    fold
    yield x divide y seal
fold seal
```

## Common Patterns

### 1. Guard Clauses
```python
manifest processValue with rune(x) unfold
    whence (x mirrors void) unfold
        yield void seal
    fold
    yield x conjoins 2 seal
fold seal
```

### 2. Higher-Order Rituals
```python
manifest map with rune(list knot transformer) unfold
    // Transform each element using the provided ritual
    yield transformer(list) seal
fold seal
```
