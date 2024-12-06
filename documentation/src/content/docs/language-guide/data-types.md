---
title: Data Types
description: Overview of PyFly's data types and type system
---

# Data Types

PyFly has a simple but effective type system that includes basic data types common in most programming languages.

## Basic Types

### Integer

Integers are whole numbers:

```python
let x = 42;
let y = -17;
let z = 0;
```

### Boolean

Boolean values can be either `true` or `false`:

```python
let isTrue = true;
let isFalse = false;
let result = 5 > 3;  // evaluates to true
```

### Function

Functions are first-class citizens in PyFly:

```python
let add = fn(x, y) {
    return x + y;
};

let multiply = fn(x, y) {
    return x * y;
};
```

## Type System

PyFly uses a static type system where types are inferred from the values and operations:

```python
let x = 5;              // inferred as integer
let isValid = true;     // inferred as boolean
let add = fn(x, y) {    // inferred as function
    return x + y;
};
```

## Type Operations

### Type Coercion

PyFly does not perform implicit type coercion. Operations must be performed between values of the same type:

```python
let x = 5;
let y = true;
// x + y would result in an error
```

### Type Checking

Type checking is performed at runtime:

```python
let x = 5;
let y = 10;
x + y;    // valid: both are integers

let z = true;
x + z;    // invalid: cannot add integer and boolean
```

## Working with Types

### Function Types

Functions can take any type as arguments and return any type:

```python
// Function that takes two integers and returns an integer
let add = fn(x, y) {
    return x + y;
};

// Function that takes a boolean and returns a boolean
let not = fn(x) {
    return !x;
};
```

### Type Composition

You can create more complex types by composing functions:

```python
// Higher-order function that returns a function
let makeAdder = fn(x) {
    return fn(y) {
        return x + y;
    };
};

let addFive = makeAdder(5);
let result = addFive(10);  // returns 15
```

## Best Practices

1. Be explicit about the types you expect in function parameters
2. Use meaningful variable names that indicate the type
3. Keep type conversions explicit
4. Document expected types in comments for complex functions

## Common Patterns

### Type Guards

When working with different types, use if statements as type guards:

```python
let processValue = fn(x) {
    if (isNumber(x)) {
        return x + 1;
    } else if (isBoolean(x)) {
        return !x;
    } else {
        return x;
    }
};
```

### Type-Safe Operations

Always ensure operations are performed between compatible types:

```python
let safeAdd = fn(x, y) {
    if (isNumber(x) && isNumber(y)) {
        return x + y;
    } else {
        return null;
    }
};
```

## Future Extensions

The type system is designed to be extensible. Future versions of PyFly may include:

1. String type
2. Array type
3. Custom user-defined types
4. Type annotations
5. Compile-time type checking 