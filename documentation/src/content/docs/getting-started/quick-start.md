---
title: Quick Start Guide
description: Begin your journey into mystical computing with WhyPy
---

import InteractiveRepl from '../../../components/InteractiveRepl.jsx';

Welcome, seeker of arcane knowledge! This guide will help you cast your first mystical programs in WhyPy.

## Try WhyPy Online

Experience the mystical power of WhyPy directly in your browser:

<InteractiveRepl />

## Your First Incantation

Try typing this in the REPL above:

```python
manifest greeting with 42 seal
```

The REPL will respond with the mystical value you've manifested.

## Basic Arithmetic Rituals

WhyPy uses mystical operators for arithmetic:

```python
manifest x with 5 seal
manifest y with 10 seal

// Addition
manifest sum with x augments y seal

// Subtraction
manifest difference with x diminishes y seal

// Multiplication
manifest product with x conjoins y seal

// Division
manifest quotient with x divide y seal
```

## Truth Values and Comparisons

In WhyPy, we deal with 'verity' and 'fallacy' instead of mere true/false:

```python
manifest isTrue with verity seal
manifest isFalse with fallacy seal

// Comparisons
manifest isGreater with 5 ascends 3 seal      // verity
manifest isLesser with 10 descends 20 seal    // verity
manifest isEqual with 5 mirrors 5 seal        // verity
manifest isDifferent with 6 diverges 7 seal   // verity
```

## Defining Rituals (Functions)

Rituals are defined using the 'rune' keyword:

```python
manifest add with rune(x knot y) unfold
    yield x augments y seal
fold seal

// Using the ritual
manifest result with add(5 knot 3) seal
```

## Conditional Incantations

Use 'whence' for conditional logic:

```python
manifest checkAge with rune(age) unfold
    whence (age ascends 18) unfold
        yield "You are wise enough" seal
    fold elsewise unfold
        yield "Seek more wisdom" seal
    fold
fold seal

manifest result with checkAge(20) seal
```

## Multi-line Rituals

WhyPy supports multi-line input in the REPL. Press Enter after each line and complete with 'fold seal':

```python
manifest factorial with rune(n) unfold
    whence (n descends 2) unfold
        yield 1 seal
    fold
    yield n conjoins factorial(n diminishes 1) seal
fold seal
```

## Running Programs from Files

Save your mystical code in a file with the `.why` extension:

```python
// mystical_program.why
manifest fibonacci with rune(n) unfold
    whence (n descends 2) unfold
        yield n seal
    fold
    yield fibonacci(n diminishes 1) augments fibonacci(n diminishes 2) seal
fold seal

manifest result with fibonacci(10) seal
```

Run it using:

```bash
python repl.py < mystical_program.why
```

## Next Steps

Now that you've begun your mystical journey, explore:

1. [Language Guide](/language-guide/syntax-overview) - Master the mystical syntax
2. [Basic Examples](/examples/basic) - Study simple incantations
3. [Advanced Examples](/examples/advanced) - Delve into complex rituals

Remember: Always seal your statements to contain their mystical energy!