```python
import re

VULNERABLE_PATTERN = r"^(a+)+$"

def validate_input(value):
    pattern = re.compile(VULNERABLE_PATTERN)
    return bool(pattern.search(value))

if __name__ == "__main__":
    print(validate_input("aaaa"))
```
