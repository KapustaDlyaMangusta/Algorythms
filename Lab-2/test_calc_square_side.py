import unittest

from calc_square_side import calc_square_side


class TestCalcSquareSide(unittest.TestCase):

    def test1(self):
        N, W, H = 10, 2, 3
        result = calc_square_side(N, W, H)
        print(result)
        self.assertEqual(9, result)

    def test2(self):
        N, W, H = 2, 1000000000, 999999999
        result = calc_square_side(N, W, H)
        print(result)
        self.assertEqual(1999999998, result)

    def test3(self):
        N, W, H = 4, 1, 1
        result = calc_square_side(N, W, H)
        print(result)
        self.assertEqual(2, result)


if __name__ == "__main__":
    unittest.main()
