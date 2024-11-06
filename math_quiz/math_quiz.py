import random

def get_random_integer(min, max):
    """Generates a random integer within a specified range.

    Args:
        min (int): The minimum value for the random integer.
        max (int): The maximum value for the random integer.

    Returns:
        int: A randomly selected integer between `min` and `max`.
    """
    try:
        if not isinstance(min, int) or not isinstance(max, int):
            raise TypeError("Both min and max must be integers.")
        if min > max:
            raise ValueError("min cannot be greater than max.")
        return random.randint(min, max)
    
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None


def get_random_operator():
    """Selects a random mathematical operator.

    Returns:
        str: A randomly chosen operator, one of '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def evaluate_expression(num1, num2, operator):
    """Creates and evaluates a mathematical expression based on two numbers and an operator.

    Args:
        num1 (int or float): The first number in the expression.
        num2 (int or float): The second number in the expression.
        operator (str): The operator to use in the expression ('+', '-', '*').

    Returns:
        tuple: A tuple containing:
            - expression (str): A string representing the mathematical expression (e.g., "5 + 3").
            - result (int or float): The result of applying the operator to `num1` and `num2`.
            
    #! Raises:
        #! ValueError: If the operator is not one of '+', '-', or '*'.
    """
    try:
        # Check if num1 and num2 are valid numbers (either int or float)
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Both num1 and num2 must be integers or floats.")
        
        # Create a string representation of the expression 
        expression = f"{num1} {operator} {num2}"
        
        # Perform the calculation based on the operator provided
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        else:
            # Raise an error if the operator is not recognized
            raise ValueError("Operator must be one of '+', '-', or '*'")
        
        # Return both the expression string and the calculated result as a tuple
        return expression, result

    except (ValueError, TypeError, ZeroDivisionError) as e:
        # Catch the specific exceptions and print an error message
        print(f"Error: {e}")
        return None, None

def math_quiz():
    """Starts and runs the Math Quiz Game, where the user is asked random math questions.

    The player is presented with a series of math problems, where they must input the correct answers.
    The game will track the player's score and provide feedback after each question.
    At the end of the game, the player's score is displayed.

    Args:
        None

    Returns:
        None

    Example:
        The game will ask the user to answer questions such as:
        "Question: 5 + 3"
        The user inputs their answer, and feedback is provided based on whether the answer is correct.

    Notes:
        - The game currently asks 3 questions (can be modified by changing `total_questions`).
        - The questions include addition, subtraction, and multiplication operations.
    """

    # Initialize the player's score to 0 at the start of the game
    score = 0

    # Set the total number of questions in the quiz
    total_questions = 3

    # Welcome user and explain quiz
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for question in range(total_questions):

        # Get two random integers and a random operator
        num1 = get_random_integer(1, 10) 
        num2 = get_random_integer(1, 5) 
        operator = get_random_operator()

        # create problem and calculate solution
        PROBLEM, ANSWER = evaluate_expression(num1, num2, operator)
        
        print(f"\nQuestion: {PROBLEM}")

        # Ask user for input of solution to the problem
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)  # Try converting user input to an integer
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        # Check whetcher answer of user was correct and give feedback to user
        if useranswer == ANSWER:
            print("Correct! You earned a point.")

            # update score 
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # Display the final score to the player at the end of the game
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
