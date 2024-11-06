import unittest
from math_quiz import get_random_integer, get_random_operator, evaluate_expression


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        """Test if random numbers generated are within the specified range"""

        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        """Test that get_random_operator always returns one of the expected operators."""

        valid_operators = ['+', '-', '*']
        
        # Call the function multiple times to ensure consistency
        for _ in range(1000):  # Test the function multiple times to check randomness
            operator = get_random_operator()
            self.assertIn(operator, valid_operators, "Operator is not one of the expected values")

    def test_evaluate_expression(self):
            """Tests the `evaluate_expression` function for correct functionality and error handling."""

            test_cases = [
            # Basic operation cases
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            
            # Edge cases with zero
            (0, 5, '+', '0 + 5', 5),
            (0, 5, '-', '0 - 5', -5),
            (0, 5, '*', '0 * 5', 0),
            
            # Negative numbers
            (-5, 3, '+', '-5 + 3', -2),
            (5, -3, '-', '5 - -3', 8),
            (-5, -3, '*', '-5 * -3', 15),
        ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                expression, result = evaluate_expression(num1, num2, operator)

                # Check the expression
                self.assertEqual(expected_problem, expression, msg = f"The determined expression is not equal to the expected expression")
                # Check the solution
                self.assertEqual(expected_answer, result, msg = f"The determined expression is not equal to the expected expression")

            # Test with invalid num1 type
            expression, result = evaluate_expression("5", 3, '+')
            self.assertIsNone(expression)
            self.assertIsNone(result)

            # Test with invalid num2 type
            expression, result = evaluate_expression(5, "3", '-')
            self.assertIsNone(expression)
            self.assertIsNone(result)

            # Test with invalid types for both num1 and num2
            expression, result = evaluate_expression("5", "3", '*')
            self.assertIsNone(expression)
            self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
