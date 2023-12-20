import math
import unittest
def calculate_values(x):
    square_power = x ** 2

    return square_power
def calculate_values1(x):
    square_root = math.sqrt(x)
    return square_root
def calculate_values2(x):
    square_area = x ** 2
    return  square_area
def calculate_values3(x):

    square_perimeter = 4 * x
    return square_perimeter
def theorem_pythagoras_gipotenyza1(k1, k2):
    return k1 ** 2 + k2 ** 2
def theorem_pythagoras_katet1(k3, k2):
    return k3 ** 2 - k2 ** 2
def theorem_pythagoras_katet2(k3, k1):
    return k3 ** 2 - k1 ** 2

class TestCalculateValues(unittest.TestCase):

    def test_square_power(self):
        result0 = calculate_values(5)
        self.assertEqual(result0, 25)
    def test_square_power1(self):
        result0 = calculate_values(4)
        self.assertEqual(result0, 25)

    def test_square_root(self):
        result1 = calculate_values1(9)
        self.assertEqual(result1, 3)
    def test_square_root1(self):
        result1 = calculate_values1(4)
        self.assertEqual(result1, 3)

    def test_square_area(self):
        result2 = calculate_values2(6)
        self.assertEqual(result2, 36)

    def test_square_area1(self):
        result2 = calculate_values2(5)
        self.assertEqual(result2, 36)
    def test_square_perimeter(self):
        result3 = calculate_values3(4)
        self.assertEqual(result3, 16)
    def test_square_perimeter1(self):
        result3 = calculate_values3(3)
        self.assertEqual(result3, 16)
    def test_theorem_pythagoras_katet1(self):
        self.assertEqual(theorem_pythagoras_katet1(6, 4), 20)
    def test_theorem_pythagoras_katet1_1(self):
        self.assertEqual(theorem_pythagoras_katet1(3, 4), 25)
    def test_theorem_pythagoras_katet2(self):
        self.assertEqual(theorem_pythagoras_katet2(5, 3), 16)

    def test_theorem_pythagoras_katet2_1(self):
        self.assertEqual(theorem_pythagoras_katet2(8, 5), 20)
    def test_pythagoras_gipotenyza(self):
        self.assertEqual(theorem_pythagoras_gipotenyza1(6, 4), 52)

    def test_pythagoras_gipotenyza1(self):
        self.assertEqual(theorem_pythagoras_gipotenyza1(5, 7), 60)




if __name__ == '__main__':
    unittest.main()