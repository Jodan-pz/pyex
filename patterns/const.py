import calendar
import os

a = calendar.MONDAY

print("%d" % a)
print(f"Value is: {a}")

c = frozenset(range(12))

print(c)

print(os.path.dirname(__file__))
print(__name__)