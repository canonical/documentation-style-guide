This example should result in two warnings.

# The heading should be ignored

This line that contain # and // in the middle should also be ignored.

```python
# This line should be ignored
print("Hello, world!")  # This line should be flagged
```

```python
# This line should be ignored
print("Hello, world!") 
```

```java
// This line should be ignored
System.out.println("Hello World"); // This line should be flagged
```