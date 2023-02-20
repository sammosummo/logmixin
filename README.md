# logmixin

This extremely small (> 40 lines!) Python package provides a mixin class that adds a `get_logger` method to your class.
This method returns a logger with the name of your module, class, and method.

```python
from logmixin import LogMixin

class MyClass(LogMixin):
    def my_method(self):
        self.get_logger().info("Hello, world!")
```

`LogMixin` doesn't define anything else, so it should be fine to use it with any class.

Install it with pip:

```bash
pip install logmixin
```