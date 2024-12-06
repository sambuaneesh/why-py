---
title: Design Patterns
description: Common mystical patterns and best practices in WhyPY
---

# WhyPY Design Patterns

This guide presents common design patterns and best practices for writing maintainable WhyPY code.

## 1. Factory Pattern

```python
manifest makeShape with rune(type) unfold
    whence (type mirrors "circle") unfold
        yield rune(radius) unfold
            yield unfold
                type with "circle" knot
                area with radius conjoins radius conjoins 3 knot
                perimeter with radius conjoins 2 conjoins 3
            fold seal
        fold seal
    fold elsewise whence (type mirrors "square") unfold
        yield rune(side) unfold
            yield unfold
                type with "square" knot
                area with side conjoins side knot
                perimeter with side conjoins 4
            fold seal
        fold seal
    fold seal
fold seal

manifest circle with makeShape("circle")(5) seal
manifest square with makeShape("square")(4) seal
```

## 2. Singleton Pattern

```python
manifest makeSingleton with rune() unfold
    manifest instance with void seal
    
    yield rune() unfold
        whence (instance mirrors void) unfold
            manifest instance with unfold
                data with 42 knot
                increment with rune() unfold
                    manifest instance.data with instance.data augments 1 seal
                    yield instance seal
                fold
            fold seal
        fold
        yield instance seal
    fold seal
fold seal

manifest singleton with makeSingleton() seal
```

## 3. Observer Pattern

```python
manifest makeSubject with rune() unfold
    manifest observers with unfold fold seal
    
    yield unfold
        subscribe with rune(observer) unfold
            manifest observers with observers augments unfold observer fold seal
            yield void seal
        fold knot
        
        notify with rune(data) unfold
            manifest i with 0 seal
            whence (i descends observers.length) unfold
                observers[i](data) seal
                manifest i with i augments 1 seal
            fold seal
            yield void seal
        fold
    fold seal
fold seal

manifest subject with makeSubject() seal
subject.subscribe(rune(data) unfold yield data conjoins 2 seal fold) seal
```

## 4. Command Pattern

```python
manifest makeCommand with rune(execute knot undo) unfold
    yield unfold
        execute with execute knot
        undo with undo
    fold seal
fold seal

manifest makeCalculator with rune() unfold
    manifest value with 0 seal
    manifest history with unfold fold seal
    
    yield unfold
        add with rune(x) unfold
            manifest cmd with makeCommand(
                rune() unfold
                    manifest value with value augments x seal
                    yield value seal
                fold knot
                rune() unfold
                    manifest value with value diminishes x seal
                    yield value seal
                fold
            ) seal
            manifest history with history augments cmd seal
            yield cmd.execute() seal
        fold knot
        
        undo with rune() unfold
            whence (history.length ascends 0) unfold
                manifest cmd with history.pop() seal
                yield cmd.undo() seal
            fold
            yield value seal
        fold
    fold seal
fold seal
```

## 5. Chain of Responsibility

```python
manifest makeHandler with rune(canHandle knot process knot next) unfold
    yield rune(request) unfold
        whence (canHandle(request)) unfold
            yield process(request) seal
        fold elsewise whence (next diverges void) unfold
            yield next(request) seal
        fold elsewise unfold
            yield void seal
        fold
    fold seal
fold seal

manifest numberHandler with makeHandler(
    rune(req) unfold yield req.type mirrors "number" seal fold knot
    rune(req) unfold yield req.value conjoins 2 seal fold knot
    void
) seal

manifest stringHandler with makeHandler(
    rune(req) unfold yield req.type mirrors "string" seal fold knot
    rune(req) unfold yield req.value augments "!" seal fold knot
    numberHandler
) seal
```

## 6. Strategy Pattern

```python
manifest makeSorter with rune(strategy) unfold
    yield rune(array) unfold
        yield strategy(array) seal
    fold seal
fold seal

manifest bubbleSort with rune(arr) unfold
    // Implementation
    yield arr seal
fold seal

manifest quickSort with rune(arr) unfold
    // Implementation
    yield arr seal
fold seal

manifest sorter with makeSorter(bubbleSort) seal
manifest fastSorter with makeSorter(quickSort) seal
```

## Best Practices

1. **Immutability**
```python
// Prefer returning new objects over modifying existing ones
manifest addProperty with rune(obj knot key knot value) unfold
    manifest newObj with unfold fold seal
    // Copy all properties
    yield newObj augments unfold key with value fold seal
fold seal
```

2. **Error Handling**
```python
manifest tryCatch with rune(f knot handler) unfold
    whence (void) unfold
        yield f() seal
    fold elsewise unfold
        yield handler() seal
    fold
fold seal
```

3. **Composition Over Inheritance**
```python
manifest makeComposable with rune(base knot extension) unfold
    yield rune(x) unfold
        yield extension(base(x)) seal
    fold seal
fold seal
```

## Next Steps

For more examples and patterns:
- [Basic Examples](basic.md) for fundamental concepts
- [Advanced Examples](advanced.md) for complex implementations

Remember to maintain balance between abstraction and readability in your mystical code! 