import calendar
import os
from pprint import pprint

a = calendar.MONDAY

print("%d" % a)
print(f"Value is: {a}")

c = frozenset(range(12))

print(c)

print(os.path.dirname(__file__))
print(__name__)

loll = {"a": 12, "x": [12, 3, 2, 4], "pol": (12, 3, 4,)}
pprint(loll, sort_dicts=0)
print(loll)


def x(a, b, c): return f"{a},{b} {c}"


print(x(1, 2, 3))
