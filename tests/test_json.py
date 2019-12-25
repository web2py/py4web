import datetime
import json
import unittest
import fractions

from py4web.core import dumps, objectify


class TestJson(unittest.TestCase):
    def test_objectify(self):
        """Check if we can serialize objects, generators, and dates"""

        class A(object):
            def __init__(self, x):
                self.x = x

        def f(n):
            for k in range(n):
                yield k + 1

        b = {
            "numbers": f(3),
            "aaa": [A(k) for k in range(3)],
            "date": datetime.date(2018, 12, 31),
        }
        c = dumps(b)
        d = {
            "numbers": [1, 2, 3],
            "aaa": [
                {"__class__": "A", "x": 0},
                {"__class__": "A", "x": 1},
                {"__class__": "A", "x": 2},
            ],
            "date": "2018-12-31",
        }
        self.assertEqual(json.loads(c), d)

        self.assertEqual(objectify(1), 1)
        self.assertEqual(objectify(fractions.Fraction(3, 2)), 1.5)
        self.assertEqual(objectify("hello"), "hello")
