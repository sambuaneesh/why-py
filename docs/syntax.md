# WhyPY Syntax Overview

## Basic Structure

WhyPY code is composed of mystical statements, each sealed with the `seal` keyword to contain their power:

```python
manifest x with 5 seal
manifest y with 10 seal
```

## Core Concepts

### Manifestations (Variables)

Variables are manifested into existence using the `manifest` keyword:

```python
manifest name with "mystic" seal
manifest value with 42 seal
manifest truth with verity seal
```

### Rituals (Functions)

Functions are defined as rituals using the `rune` keyword:

```python
manifest add with rune(x knot y) unfold
    yield x augments y seal
fold seal
```

### Control Flow

#### Whence-Elsewise (If-Else)

Conditional execution uses the `whence` and `elsewise` keywords:

```python
whence (x ascends y) unfold
    yield verity seal
fold elsewise unfold
    yield fallacy seal
fold
```

### Operators

| Operation | Keyword | Example |
|-----------|---------|---------|
| Addition | `augments` | `x augments y` |
| Subtraction | `diminishes` | `x diminishes y` |
| Multiplication | `conjoins` | `x conjoins y` |
| Division | `divide` | `x divide y` |
| Less Than | `descends` | `x descends y` |
| Greater Than | `ascends` | `x ascends y` |
| Equals | `mirrors` | `x mirrors y` |
| Not Equals | `diverges` | `x diverges y` |
| Logical NOT | `negate` | `negate x` |

## Block Structure

Code blocks are marked by `unfold` and `fold`:

```python
manifest ritual with rune() unfold
    manifest x with 5 seal
    manifest y with 10 seal
    yield x augments y seal
fold seal
```

## Comments

Comments are marked with `//`:

```python
// This is a mystical comment
manifest x with 42 seal  // The answer to everything
```

## Error Handling

Errors are treated as mishaps in the flow of mystical energy:

```python
whence (x mirrors void) unfold
    yield "Mishap: Cannot proceed with void" seal
fold
```

## Complete Example

Here's a complete example showing various syntax elements:

```python
// Define a ritual to calculate mystical power
manifest calculatePower with rune(base knot exponent) unfold
    whence (exponent descends 0) unfold
        yield 1 seal
    fold
    
    manifest result with base seal
    manifest count with 1 seal
    
    whence (count descends exponent) unfold
        manifest result with result conjoins base seal
        manifest count with count augments 1 seal
    fold
    
    yield result seal
fold seal

// Use the ritual
manifest power with calculatePower(2 knot 3) seal  // Results in 8
```

For more examples and detailed explanations, see:
- [Basic Rituals](examples/basic.md)
- [Advanced Incantations](examples/advanced.md)
- [Mystical Patterns](examples/patterns.md) 