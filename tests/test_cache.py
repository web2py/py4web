import random
import time
import unittest

import py4web


class CacheTest(unittest.TestCase):
    def test_logic(self):
        cache = py4web.Cache()
        cache.get("x", lambda: "y")
        self.assertEqual(cache.head.next.next, cache.tail)
        self.assertEqual(cache.head.next, cache.tail.prev)
        self.assertEqual(cache.head, cache.tail.prev.prev)
        self.assertEqual(cache.head.next.key, "x")
        self.assertEqual(cache.head.next.value, "y")

    def test_different_keys(self):
        cache = py4web.Cache()
        results = set()
        for k in range(100):
            results.add(cache.get("a", random.random))
            results.add(cache.get("b", random.random))
            results.add(cache.get("c", random.random))
        self.assertEqual(len(results), 3)

    def test_change_detection(self):
        cache = py4web.Cache()
        results = set()
        for k in range(30):
            results.add(
                cache.get("a", random.random, expiration=0, monitor=lambda: int(k / 10))
            )
        self.assertEqual(len(results), 3)
        time.sleep(0.02)
        results.add(cache.get("a", random.random, expiration=0.01, monitor=lambda: 5))
        self.assertEqual(len(results), 4)

    def test_timing(self):
        M = N = 100000
        cache = py4web.Cache()
        for k in range(M):
            cache.get(k, random.random)
        t0 = time.time()
        for k in range(N):
            cache.get("new", random.random)
        self.assertTrue((time.time() - t0) / N, 1 - 5)
        self.assertTrue(cache.free == 0)

    def test_memoize_and_expiration(self):
        memoize = py4web.Cache().memoize(expiration=0.1)

        @memoize
        def f(x):
            return x + random.random()

        results = set()
        for k in range(10):
            results.add(f(1))
            results.add(f(2))
        time.sleep(0.2)
        for k in range(10):
            results.add(f(1))
            results.add(f(2))
        self.assertEqual(len(results), 4)
