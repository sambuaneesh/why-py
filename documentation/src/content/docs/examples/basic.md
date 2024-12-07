---
title: Basic Examples
description: Fundamental WhyPY examples to start your mystical journey
---

import InteractiveRepl from '../../../components/InteractiveRepl';

# Basic WhyPY Examples

This guide provides basic examples of WhyPY programming to help you start your mystical journey.

## Interactive Examples

Try these examples directly in your browser:

<div client:only="react">
  <InteractiveRepl client:only="react" />
</div>

## 1. Hello, Mystic World

```python
manifest greeting with "Greetings, seeker of truth" seal

manifest sayHello with rune(name) unfold
    manifest message with greeting augments name seal
    yield message seal
fold seal

sayHello("mystic one") seal
```

## 2. Basic Arithmetic

```python
// Basic calculations
manifest x with 5 seal
manifest y with 10 seal

manifest sum with x augments y seal
manifest difference with x diminishes y seal
manifest product with x conjoins y seal
manifest quotient with y divide x seal

// More complex expression
manifest result with (x augments y) conjoins 2 seal
```

## 3. Conditional Logic

```python
manifest age with 25 seal

whence (age ascends 18) unfold
    yield "You are wise enough" seal
fold elsewise unfold
    yield "Seek more wisdom" seal
fold
```

## 4. Simple Loop Using Recursion

```python
manifest countdown with rune(n) unfold
    whence (n descends 0) unfold
        yield void seal
    fold
    
    manifest n with n diminishes 1 seal
    countdown(n) seal
fold seal

countdown(5) seal
```

## 5. Basic Function (Ritual) Usage

```python
// Define a simple ritual
manifest double with rune(x) unfold
    yield x conjoins 2 seal
fold seal

// Use the ritual
manifest result with double(5) seal  // Results in 10
```

## 6. Truth Values

```python
manifest isTrue with verity seal
manifest isFalse with fallacy seal

// Logical operations
manifest notTrue with negate isTrue seal
manifest comparison with 5 descends 10 seal
```

## 7. Basic Error Handling

```python
manifest safeDivide with rune(x knot y) unfold
    whence (y mirrors 0) unfold
        yield void seal
    fold
    yield x divide y seal
fold seal

// Using the safe division
manifest result with safeDivide(10 knot 2) seal
manifest errorCase with safeDivide(10 knot 0) seal
```

## 8. Working with Multiple Returns

```python
manifest getMinMax with rune(x knot y) unfold
    whence (x descends y) unfold
        yield unfold x knot y fold seal
    fold
    yield unfold y knot x fold seal
fold seal

manifest min knot max with getMinMax(5 knot 10) seal
```

## 9. Basic Composition

```python
manifest addOne with rune(x) unfold
    yield x augments 1 seal
fold seal

manifest multiplyByTwo with rune(x) unfold
    yield x conjoins 2 seal
fold seal

// Compose the rituals
manifest result with multiplyByTwo(addOne(5)) seal
```

## 10. Simple Calculator

```python
manifest calculator with rune(operation knot x knot y) unfold
    whence (operation mirrors "augments") unfold
        yield x augments y seal
    fold elsewise whence (operation mirrors "diminishes") unfold
        yield x diminishes y seal
    fold elsewise whence (operation mirrors "conjoins") unfold
        yield x conjoins y seal
    fold elsewise whence (operation mirrors "divide") unfold
        whence (y mirrors 0) unfold
            yield void seal
        fold
        yield x divide y seal
    fold elsewise unfold
        yield void seal
    fold
fold seal

// Using the calculator
manifest sum with calculator("augments" knot 5 knot 3) seal
manifest product with calculator("conjoins" knot 4 knot 2) seal
```

## Next Steps

Once you're comfortable with these basic examples, proceed to:
- [Advanced Examples](advanced.md) for more complex patterns
- [Design Patterns](patterns.md) for common programming patterns in WhyPY

Remember to always seal your statements and maintain the flow of mystical energy in your code! 