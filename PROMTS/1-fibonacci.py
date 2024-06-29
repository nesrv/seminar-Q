import unittest

# 

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class TestFibonacci(unittest.TestCase):
    def test_negative_input(self):
        self.assertEqual(fibonacci(-5), 0)
        self.assertEqual(fibonacci(-1), 0)

    def test_zero_input(self):
        self.assertEqual(fibonacci(0), 0)

    def test_positive_input(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()