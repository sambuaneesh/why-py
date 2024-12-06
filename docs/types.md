# WhyPY Data Types

WhyPY implements a mystical type system that represents the fundamental building blocks of computational reality.

## Core Types

### NUMBER (Integer)

The most basic form of quantifiable mystical energy:

```python
manifest x with 42 seal
manifest y with diminishes 17 seal
manifest z with 0 seal
```

Operations:

```python
manifest sum with x augments y seal
manifest product with x conjoins y seal
manifest quotient with x divide y seal
manifest difference with x diminishes y seal
```

### TRUTH (Boolean)

The duality of existence, represented by `verity` and `fallacy`:

```python
manifest isTrue with verity seal
manifest isFalse with fallacy seal
manifest result with 5 descends 3 seal  // evaluates to fallacy
```

Operations:

```python
manifest negation with negate verity seal  // fallacy
manifest comparison with verity mirrors verity seal  // verity
manifest difference with verity diverges fallacy seal  // verity
```

### RITUAL (Function)

Rituals are first-class values that can transform and manipulate other values:

```python
manifest add with rune(x knot y) unfold
    yield x augments y seal
fold seal

manifest makeMultiplier with rune(factor) unfold
    yield rune(x) unfold
        yield x conjoins factor seal
    fold seal
fold seal
```

### VOID (Null)

The absence of value, the mystical void:

```python
manifest empty with void seal

whence (empty mirrors void) unfold
    yield "Found the void" seal
fold
```

## Type System Features

### Dynamic Typing

WhyPY uses dynamic typing, determining types during the ritual of evaluation:

```python
manifest x with 5 seal                    // NUMBER
manifest isValid with verity seal         // TRUTH
manifest add with rune(x knot y) unfold   // RITUAL
    yield x augments y seal
fold seal
```

### Type Verification

The interpreter verifies types during evaluation to prevent mystical mishaps:

```python
manifest x with 5 seal
manifest y with verity seal
x augments y seal    // MISHAP: Cannot augment NUMBER with TRUTH
```

### Type Coercion

WhyPY does not perform automatic type coercion, maintaining the purity of each type:

```python
manifest x with 5 seal
manifest y with "10" seal
x augments y seal    // MISHAP: Cannot augment NUMBER with TEXT
```


## Error Handling

WhyPY provides clear mishap messages for type-related issues:

```python
// Type mismatch
MISHAP: Cannot augment NUMBER with TRUTH

// Undefined operation
MISHAP: Operation 'conjoins' not defined for TRUTH values

// Invalid ritual call
MISHAP: Cannot invoke NUMBER as ritual
```

## Advanced Type Patterns

### Type Checking

```python
manifest isNumber with rune(x) unfold
    whence (x mirrors void) unfold
        yield fallacy seal
    fold
    yield x conjoins 1 mirrors x conjoins 1 seal  // Only works for NUMBER
fold seal
```

### Optional Values

```python
manifest findValue with rune(key) unfold
    whence (key mirrors void) unfold
        yield void seal
    fold
    // ... search for value ...
fold seal
```

For more examples and patterns, see:
- [Basic Type Usage](examples/basic.md)
- [Advanced Type Patterns](examples/advanced.md)
- [Type Safety Patterns](examples/patterns.md) 