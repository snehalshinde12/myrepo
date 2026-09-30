```python
import re

# INTENTIONALLY VULNERABLE — TEST REPOSITORY ONLY
# ReDoS / CWE-1333 test case

VULNERABLE_PATTERN = r"^(a+)+$"

def validate_input(value):
    pattern = re.compile(VULNERABLE_PATTERN)
    return bool(pattern.search(value))


if __name__ == "__main__":
    print(validate_input("aaaa"))
```
