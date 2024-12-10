---
title: Basic Examples
description: Fundamental WhyPY examples to start your mystical journey
---

# Basic WhyPY Examples

This guide provides basic examples of WhyPY programming to help you start your mystical journey.

## Interactive Examples


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
manifest fibonacci with rune(n) unfold
    whence (n descends 2) unfold
        yield n seal
    fold

    yield fibonacci(n diminishes 1) augments fibonacci(n diminishes 2) seal
fold seal

manifest result with fibonacci(10) seal 
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


## 7. Basic Composition

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

## Next Steps

Once you're comfortable with these basic examples, proceed to:
- [Advanced Examples](advanced.md) for more complex patterns
- **Design Patterns** for common programming patterns in WhyPY (Coming Soon)

Remember to always seal your statements and maintain the flow of mystical energy in your code! 