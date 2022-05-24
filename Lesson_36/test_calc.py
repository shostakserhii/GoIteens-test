import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        """Testing add func with different attrs."""
        self.assertEqual(calc.add(10, 20), 30)
        self.assertEqual(calc.add(-10, 5), -5)
        self.assertEqual(calc.add(-10, -10), -20)

    def test_subtract(self):
        """Testing subtract func with different attrs."""
        self.assertEqual(calc.subtract(20, 10), 10)
        self.assertEqual(calc.subtract(-10, 5), -15)
        self.assertEqual(calc.subtract(-10, -10), 0)

    def test_multiply(self):
        """Testing multiply func with different attrs."""
        self.assertEqual(calc.multiply(5, 10), 50)
        self.assertEqual(calc.multiply(-10, 5), -50)
        self.assertEqual(calc.multiply(-10, -10), 100)

    def test_divide_success(self):
        """Testing divide func with different attrs."""
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-10, 5), -2)
        self.assertEqual(calc.divide(-10, -5), 2)
        self.assertEqual(calc.divide(5.5, 2), 2.75)
        # self.assertRaises(ValueError, calc.divide, 10, 0)

    def test_divide_raises_error(self):
        """Testing divide func to raise Error."""
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
