haskell foldl foldr

自下而上  自上而下



#  corecursion is a type of operation that is dual to recursion


https://en.wikipedia.org/wiki/Corecursion#Examples



 corecursion is a type of operation that is dual to recursion





factorial recursively

```
0! := 1 and n! := n × (n - 1)!
```

```haskell
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

line x = printf "%d! = %d\n" x $ factorial x

main = mapM_ line [0..16]
```

```python
def factorial(n):
    """Recursive factorial function."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

 the factorial corecursively

$$n,f = (0,1):(n+1,f * (n+1)$$

```haskell
 (\(n,f) -> (n+1, f*(n+1))) `iterate` (0,1)
```

```python
def factorials():
    """Corecursive generator."""
    n, f = 0, 1
    while True:
        yield f
        n, f = n + 1, f * (n + 1)
```

This generates an infinite stream of factorials in order; a finite portion of it can be produced by:


```python
def n_factorials(k):
    n, f = 0, 1
    while n <= k:
        yield f
        n, f = n + 1, f * (n + 1)
```

This could then be called to produce the factorials up to 5! via:



```python
for f in n_factorials(5):
    print(f)
```


If we're only interested in a certain factorial, just the last value can be taken, or we can fuse the production and the access into one function,


```python
def nth_factorial(k):
    n, f = 0, 1
    while n < k:
        n, f = n + 1, f * (n + 1)
    yield f
```



As can be readily seen here, this is practically equivalent (just by substituting return for the only yield there) to the accumulator argument technique for tail recursion, unwound into an explicit loop. Thus it can be said that the concept of corecursion is an explication of the embodiment of iterative computation processes by recursive definitions, where applicable.

