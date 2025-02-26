# Watchfiles reproduction

Run [`main.py`](./main.py) with `python main.py` and watch the output.

It will never stop, and the console will show the following output:

```plain
is_set() -> True
is_set() -> False
is_set() -> False
is_set() -> False
is_set() -> False
...
```

But if you move the `from watchfiles import watch` line to the top of the file, everything will be fine.

Or removing the `del self._event` line will also fix the issue.

That's weird.

## Notes

I overloaded `is_set` to print a message every time it is called.

```py
class Event(threading.Event):
    def is_set(self):
        value = super().is_set()
        print(f"is_set() -> {value}")
        return value
```
