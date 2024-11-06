import unittest
from math_quiz import get_random_integer, get_random_operator, evaluate_expression


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # TODO
        pass

    def test_evaluate_expression(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7)
                # TODO add more test cases here
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()
