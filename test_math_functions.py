import math
import unittest

import math_functions as mf


class MathFunctionsTest(unittest.TestCase):
    def test_basic_arithmetic(self):
        self.assertEqual(mf.add(2, 3), 5)
        self.assertEqual(mf.subtract(10, 4), 6)
        self.assertEqual(mf.multiply(6, 7), 42)
        self.assertEqual(mf.divide(9, 2), 4.5)
        self.assertEqual(mf.modulo(10, 3), 1)
        self.assertEqual(mf.floor_divide(10, 3), 3)

    def test_divide_by_zero_errors(self):
        with self.assertRaises(ValueError):
            mf.divide(1, 0)
        with self.assertRaises(ValueError):
            mf.modulo(1, 0)
        with self.assertRaises(ValueError):
            mf.floor_divide(1, 0)

    def test_powers_and_roots(self):
        self.assertEqual(mf.power(2, 5), 32)
        self.assertEqual(mf.square(9), 81)
        self.assertEqual(mf.cube(3), 27)
        self.assertEqual(mf.square_root(81), 9)
        self.assertAlmostEqual(mf.cube_root(-27), -3)
        self.assertAlmostEqual(mf.nth_root(32, 5), 2)

    def test_invalid_roots(self):
        with self.assertRaises(ValueError):
            mf.square_root(-1)
        with self.assertRaises(ValueError):
            mf.nth_root(-16, 2)
        with self.assertRaises(ValueError):
            mf.nth_root(16, 0)

    def test_number_theory_helpers(self):
        self.assertEqual(mf.factorial(5), 120)
        self.assertEqual(mf.gcd(54, 24), 6)
        self.assertEqual(mf.lcm(4, 6), 12)
        self.assertTrue(mf.is_even(8))
        self.assertTrue(mf.is_odd(9))
        self.assertTrue(mf.is_prime(97))
        self.assertFalse(mf.is_prime(1))
        self.assertFalse(mf.is_prime(100))

    def test_trig_and_log_helpers(self):
        self.assertAlmostEqual(mf.degrees_to_radians(180), math.pi)
        self.assertAlmostEqual(mf.radians_to_degrees(math.pi), 180)
        self.assertAlmostEqual(mf.sine(math.pi / 2), 1)
        self.assertAlmostEqual(mf.cosine(0), 1)
        self.assertAlmostEqual(mf.tangent(math.pi / 4), 1)
        self.assertAlmostEqual(mf.logarithm(8, 2), 3)
        self.assertAlmostEqual(mf.natural_log(math.e), 1)
        self.assertAlmostEqual(mf.log10(1000), 3)

    def test_invalid_logarithms(self):
        with self.assertRaises(ValueError):
            mf.logarithm(0)
        with self.assertRaises(ValueError):
            mf.logarithm(10, 1)

    def test_aggregate_and_percentage_helpers(self):
        self.assertEqual(mf.mean([2, 4, 6]), 4)
        self.assertEqual(mf.median([9, 1, 5]), 5)
        self.assertEqual(mf.product([2, 3, 4]), 24)
        self.assertEqual(mf.percentage(25, 200), 12.5)
        self.assertEqual(mf.percentage_change(100, 125), 25)

    def test_empty_aggregate_errors(self):
        with self.assertRaises(ValueError):
            mf.mean([])
        with self.assertRaises(ValueError):
            mf.median([])
        with self.assertRaises(ValueError):
            mf.product([])

    def test_misc_helpers(self):
        self.assertEqual(mf.absolute(-42), 42)
        self.assertEqual(mf.reciprocal(4), 0.25)
        self.assertEqual(mf.clamp(12, 0, 10), 10)
        self.assertEqual(mf.clamp(-1, 0, 10), 0)
        self.assertEqual(mf.clamp(5, 0, 10), 5)
        self.assertEqual(mf.round_to(3.14159, 2), 3.14)

        with self.assertRaises(ValueError):
            mf.reciprocal(0)
        with self.assertRaises(ValueError):
            mf.clamp(5, 10, 0)


if __name__ == "__main__":
    unittest.main()
