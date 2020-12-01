import unittest


def a(x):
    def b(y):
        return x + y

    return b


class TestSumMethods(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(a(3)(4), 7)
        self.assertEqual(a(3)(1), 7)

    def test_sub(self):
        self.assertGreater(a(1)(1), 3)


if __name__ == '__main__':
    unittest.main()
