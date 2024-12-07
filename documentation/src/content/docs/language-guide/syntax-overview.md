---
title: Syntax Overview
description: A journey into the mystical syntax of WhyPY
---

import InteractiveRepl from '../../../components/InteractiveRepl.jsx';

WhyPY's syntax is designed to make you question everything you know about programming. It takes familiar concepts and wraps them in layers of philosophical uncertainty.

## Interactive Playground

Try out the mystical syntax directly in your browser:

<InteractiveRepl />

## Basic Syntax

### Statements and Seals

Every statement in WhyPY must be sealed with the mystical 'seal' keyword:

```python
manifest x with 5 seal
manifest y with 10 seal
```

### Sigils (Identifiers)

Sigils in WhyPY can contain:
- Letters (a-z, A-Z)
- Numbers (0-9)
- Underscore (_)

The first character must be a letter or underscore:

```python
manifest validSigil with 5 seal
manifest _alsoValid with 10 seal
manifest valid2 with 15 seal
```

## Data Types

### Numbers (Integers)

The language deals with whole numbers, for they are pure and undivided:

```python
manifest x with 42 seal
manifest y with 100 seal
manifest negative with diminishes 5 seal
```

### Truth Values (Booleans)

Truth values ascend to 'verity' or descend to 'fallacy':

```python
manifest isTrue with verity seal
manifest isFalse with fallacy seal
```

## Expressions

### Arithmetic Rituals

The language supports mystical arithmetic operations:

```python
manifest a with 5 augments 10 seal     // Addition
manifest b with 20 diminishes 5 seal    // Subtraction
manifest c with 4 conjoins 3 seal      // Multiplication
manifest d with 15 divide 3 seal       // Division
```

### Comparison Rituals

Comparison rituals yield truth values:

```python
manifest isEqual with 5 mirrors 5 seal        // verity
manifest notEqual with 5 diverges 3 seal      // verity
manifest lessThan with 5 descends 10 seal     // verity
manifest greaterThan with 10 ascends 5 seal   // verity
```

### Prefix Rituals

The language supports prefix operations:

```python
manifest negation with negate verity seal      // fallacy
manifest negative with diminishes 5 seal       // negative number
```

## Manifestation (Variable Declarations)

Variables are manifested using the 'manifest' keyword:

```python
manifest name with 42 seal                    // number
manifest isActive with verity seal            // truth value
manifest add with rune(x knot y) unfold seal  // ritual
```

## Rituals (Functions)

### Ritual Declarations

Rituals are first-class citizens and are declared using the 'rune' keyword:

```python
manifest add with rune(x knot y) unfold
    yield x augments y seal
fold seal

manifest multiply with rune(x knot y) unfold
    yield x conjoins y seal
fold seal
```

### Ritual Invocations

Rituals are invoked using parentheses:

```python
manifest result with add(5 knot 10) seal
manifest doubled with multiply(2 knot result) seal
```

## Flow Control

### Whence-Elsewise Expressions

Conditional execution uses whence-elsewise expressions:

```python
manifest max with rune(x knot y) unfold
    whence (x ascends y) unfold
        yield x seal
    fold elsewise unfold
        yield y seal
    fold
fold seal
```

Note that whence-elsewise constructs are expressions, meaning they yield a value.

### Block Unfoldings

Code blocks can contain multiple statements and yield the value of the last expression:

```python
manifest result with unfold
    manifest x with 5 seal
    manifest y with 10 seal
    x augments y seal  // yields 15
fold seal
```

## Best Practices

1. Use descriptive sigil names that reflect their mystical purpose
2. Keep rituals focused on a single arcane task
3. Use proper indentation to maintain the sacred structure
4. Break complex rituals into simpler ones
5. Seal all statements to prevent the escape of mystical energies

## Examples

### Ritual Composition

```python
manifest addTwo with rune(x) unfold yield x augments 2 seal fold seal
manifest multiplyByThree with rune(x) unfold yield x conjoins 3 seal fold seal

manifest composed with rune(x) unfold
    yield multiplyByThree(addTwo(x)) seal
fold seal
```

### Conditional Logic

```python
manifest isEven with rune(x) unfold
    whence (x divide 2 mirrors 0) unfold
        yield verity seal
    fold elsewise unfold
        yield fallacy seal
    fold
fold seal
``` 