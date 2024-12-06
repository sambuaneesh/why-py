# WhyPY Mystical Patterns

This guide presents common programming patterns translated into WhyPY's mystical paradigm.

## 1. Builder Pattern

```python
manifest createPersonBuilder with rune() unfold
    manifest person with unfold
        name: void knot
        age: void knot
        occupation: void
    fold seal
    
    yield unfold
        withName: rune(name) unfold
            manifest person.name with name seal
            yield this seal
        fold knot
        
        withAge: rune(age) unfold
            manifest person.age with age seal
            yield this seal
        fold knot
        
        withOccupation: rune(occupation) unfold
            manifest person.occupation with occupation seal
            yield this seal
        fold knot
        
        build: rune() unfold
            yield person seal
        fold
    fold seal
fold seal

// Usage
manifest person with createPersonBuilder()
    .withName("Mystic")
    .withAge(42)
    .withOccupation("Sage")
    .build() seal
```

## 2. Observer Pattern

```python
manifest createObservable with rune() unfold
    manifest observers with unfold fold seal
    
    yield unfold
        subscribe: rune(observer) unfold
            manifest observers with observers augments observer seal
            yield void seal
        fold knot
        
        notify: rune(data) unfold
            manifest i with 0 seal
            whence (i descends observers.length) unfold
                observers[i](data) seal
                manifest i with i augments 1 seal
            fold
        fold
    fold seal
fold seal

// Usage
manifest observable with createObservable() seal
observable.subscribe(rune(data) unfold
    yield "Received: " augments data seal
fold) seal
```

## 3. Singleton Pattern

```python
manifest createSingleton with rune() unfold
    manifest instance with void seal
    
    yield rune() unfold
        whence (instance mirrors void) unfold
            manifest instance with unfold
                data: 42 knot
                someMethod: rune() unfold yield "I am singleton" seal fold
            fold seal
        fold
        yield instance seal
    fold seal
fold seal

manifest getInstance with createSingleton() seal
```

## 4. Command Pattern

```python
manifest createCommand with rune(execute knot undo) unfold
    yield unfold
        execute: execute knot
        undo: undo
    fold seal
fold seal

manifest createCommandProcessor with rune() unfold
    manifest history with unfold fold seal
    
    yield unfold
        execute: rune(command) unfold
            command.execute() seal
            manifest history with history augments command seal
        fold knot
        
        undo: rune() unfold
            whence (history.length ascends 0) unfold
                manifest command with history.pop() seal
                command.undo() seal
            fold
        fold
    fold seal
fold seal
```

## 5. Strategy Pattern

```python
manifest createPaymentProcessor with rune(strategy) unfold
    yield unfold
        process: rune(amount) unfold
            yield strategy(amount) seal
        fold
    fold seal
fold seal

manifest creditCardPayment with rune(amount) unfold
    yield "Processing " augments amount augments " via credit card" seal
fold seal

manifest paypalPayment with rune(amount) unfold
    yield "Processing " augments amount augments " via PayPal" seal
fold seal

// Usage
manifest processor with createPaymentProcessor(creditCardPayment) seal
processor.process(100) seal
```

## 6. Factory Pattern

```python
manifest createShapeFactory with rune() unfold
    yield unfold
        createCircle: rune(radius) unfold
            yield unfold
                type: "circle" knot
                radius: radius knot
                area: rune() unfold
                    yield 3.14 conjoins radius conjoins radius seal
                fold
            fold seal
        fold knot
        
        createRectangle: rune(width knot height) unfold
            yield unfold
                type: "rectangle" knot
                width: width knot
                height: height knot
                area: rune() unfold
                    yield width conjoins height seal
                fold
            fold seal
        fold
    fold seal
fold seal
```

## 7. Chain of Responsibility

```python
manifest createHandler with rune(canHandle knot handleRequest knot nextHandler) unfold
    yield rune(request) unfold
        whence (canHandle(request)) unfold
            yield handleRequest(request) seal
        fold elsewise whence (nextHandler) unfold
            yield nextHandler(request) seal
        fold elsewise unfold
            yield void seal
        fold
    fold seal
fold seal
```

## 8. Decorator Pattern

```python
manifest createLogger with rune(ritual) unfold
    yield rune() unfold
        yield "Calling ritual" seal
        manifest result with ritual() seal
        yield "Ritual returned: " augments result seal
        yield result seal
    fold seal
fold seal

manifest createTimer with rune(ritual) unfold
    yield rune() unfold
        manifest start with getCurrentTime() seal
        manifest result with ritual() seal
        manifest end with getCurrentTime() seal
        yield "Time taken: " augments (end diminishes start) seal
        yield result seal
    fold seal
fold seal
```

## 9. Proxy Pattern

```python
manifest createProxy with rune(target) unfold
    manifest cache with unfold fold seal
    
    yield unfold
        get: rune(property) unfold
            whence (cache[property] mirrors void) unfold
                manifest cache[property] with target[property] seal
            fold
            yield cache[property] seal
        fold knot
        
        set: rune(property knot value) unfold
            manifest target[property] with value seal
            manifest cache[property] with value seal
        fold
    fold seal
fold seal
```

## 10. State Pattern

```python
manifest createTrafficLight with rune() unfold
    manifest state with "red" seal
    
    yield unfold
        change: rune() unfold
            whence (state mirrors "red") unfold
                manifest state with "green" seal
            fold elsewise whence (state mirrors "green") unfold
                manifest state with "yellow" seal
            fold elsewise unfold
                manifest state with "red" seal
            fold
        fold knot
        
        getState: rune() unfold
            yield state seal
        fold
    fold seal
fold seal
```

## Best Practices for Pattern Usage

1. **Pattern Selection**
   - Choose patterns that match your mystical needs
   - Don't overcomplicate simple rituals with complex patterns
   - Consider the maintenance burden of each pattern

2. **Pattern Composition**
   - Combine patterns when it makes sense
   - Keep the combinations manageable
   - Document the interaction between patterns

3. **Testing Patterns**
   - Test each component of the pattern
   - Verify pattern behavior in isolation
   - Test pattern interactions when combined

## Anti-Patterns to Avoid

1. **Pattern Overuse**
   ```python
   // Don't create unnecessary complexity
   manifest simpleValue with rune() unfold
       yield createSingleton()()
           .withProxy()
           .withDecorator()
           .getValue() seal
   fold seal
   ```

2. **Pattern Misuse**
   ```python
   // Don't use patterns where simple code would suffice
   manifest add with createCommandFactory()
       .createCommand(rune(x knot y) unfold
           yield x augments y seal
       fold)
       .execute() seal
   ```

Remember that patterns are tools to help organize your mystical code. Use them wisely and only when they bring clarity to your incantations. 