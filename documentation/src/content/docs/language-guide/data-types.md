---
title: Data Types
description: Understanding the mystical types that flow through WhyPY
---

# Data Types

WhyPY implements a mystical object system with fundamental types that represent the basic building blocks of computational reality.

## Basic Types

### NUMBER (Integer)

Numbers represent the quantifiable essence of reality:

```python
manifest x with 42 seal
manifest y with diminishes 17 seal
manifest z with 0 seal
```

Operations on numbers:
- Augmentation: `5 augments 3`
- Diminishment: `10 diminishes 4`
- Conjunction: `6 conjoins 7`
- Division: `15 divide 3`
- Comparison: `5 descends 10`, `7 ascends 3`, `5 mirrors 5`, `6 diverges 4`

### TRUTH (Boolean)

Truth values represent the duality of existence:

```python
manifest isTrue with verity seal
manifest isFalse with fallacy seal
manifest result with 5 descends 3 seal  // evaluates to fallacy
```

Operations on truth values:
- Negation: `negate verity` evaluates to `fallacy`
- Equality: `verity mirrors verity`, `fallacy diverges verity`

### RITUAL (Function)

Rituals are the transformative forces in WhyPY:

```python
// Simple ritual
manifest add with rune(x knot y) unfold
    yield x augments y seal
fold seal

// Ritual with multiple statements
manifest max with rune(x knot y) unfold
    whence (x ascends y) unfold
        yield x seal
    fold elsewise unfold
        yield y seal
    fold
fold seal

// Ritual that yields another ritual
manifest makeAdder with rune(x) unfold
    yield rune(y) unfold
        yield x augments y seal
    fold seal
fold seal
```

## Object System

The interpreter uses a mystical object system defined in `object.py`:

### NUMBER Objects

```python
class Integer:
    def type(self) -> str:
        return "NUMBER"
```

### TRUTH Objects

```python
class Boolean:
    def type(self) -> str:
        return "TRUTH"
```

### RITUAL Objects

```python
class Function:
    def type(self) -> str:
        return "RITUAL"
```

## Type System

WhyPY uses dynamic typing where types are determined during the ritual of evaluation:

```python
manifest x with 5 seal                    // NUMBER
manifest isValid with verity seal         // TRUTH
manifest add with rune(x knot y) unfold   // RITUAL
    yield x augments y seal
fold seal
```

### Type Verification

Type verification occurs during the ritual of evaluation:

```python
manifest x with 5 seal
manifest y with 10 seal
x augments y seal    // valid: both are numbers

manifest z with verity seal
x augments z seal    // mishap: type mismatch
```

## Mishap Handling

The interpreter includes mishap handling for type-related issues:

```python
class Error:
    def type(self) -> str:
        return "MISHAP"
```

Common mishaps:
- Type mismatches in operations
- Unknown rituals for types
- Undefined sigils
- Invalid ritual invocations

## Best Practices

1. Respect the types in your rituals
2. Handle potential mishaps in your code
3. Use sigil names that reflect their mystical type
4. Keep rituals type-consistent
5. Document expected types in complex rituals

## Examples

### Type-Safe Rituals

```python
manifest divide with rune(x knot y) unfold
    whence (y mirrors 0) unfold
        yield fallacy seal  // Mishap case
    fold
    yield x divide y seal
fold seal
```

### Ritual Composition

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