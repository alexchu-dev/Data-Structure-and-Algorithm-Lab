# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Alex Chu 
# Student Number: 153954219
#

def wins_rock_scissors_paper(player1_input, player2_input):
    """
    A simple program of rock scissors paper game. Return true when player1 wins.
    This function does not use complicated logic, it just compares two string inputs with if else.
    """
    if player1_input.lower() == "rock":
        if player2_input.lower() == "scissors":
            return True
        else:
            return False
    elif player1_input.lower() == "paper":
        if player2_input.lower() == "rock":
            return True
        else:
            return False
    elif player1_input.lower() == "scissors":
        if player2_input.lower() == "paper":
            return True
        else:
            return False


def factorial(num):
    """
    A function finding the factorial of a number using a while loop.
    when num = 1, fact * 1 is the same, so num = 0 & 1 can be skipped.
    """
    fact = 1
    while num > 1:
        fact = fact * num
        num -= 1
    return fact


# def fibonacci(num):
#     """
#     A function using recursion to find the "fibnoacci" number.
#     Using conditions for the first 2 exception numbers, starting from num > 1 it will sum up num - 1 and num - 2.
#     """
#     if num <= 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         sum_up = fibonacci(num - 1) + fibonacci(num - 2)
#     return sum_up


def fibonacci(num):
    """
        A function to find the "fibnoacci" number.
        Using conditions for the first 2 exception numbers, starting from num > 1 it will sum up num - 1 and num - 2.
    """
    # Let fn represent the nth fibonacci number i.e. f0 = 0, f1 = 1...
    fn, f0, f1 = 0, 0, 1    # 1 + 1 + 1
    if num <= 0:            # 1
        return 0            # 1
    elif num == 1:          # 1
        return 1            # 1
    else:
        for i in range(2, num + 1): # (n - 1) + 1 + 1
            fn = f1 + f0    # 2 (n - 1) Everything starts with F1 and F0 first
            f0 = f1         # (n - 1) then f0 takes the value of f1
            f1 = fn         # (n - 1) and f1 takes the value of fn, so that we don't need to do the recursion
        return fn           # 1
    # T(n) = 1 + 1 + 1 + (n - 1) + 1 + 1 + 2 (n - 1) + (n - 1) + (n - 1) + 1 = 5n + 1. i.e. T(n) is O(n).


def sum_to_goal(num_list, goal):
    """
    This function receives a list of numbers and finds out the numbers which
    sum up to the "goal" value, then it returns the product of these two number.
    I have written in a way for challenge such that if there are more than 1 pair of numbers in the list
    which also sum to the goal value, will then return as a list of product.
    E.g. ([1, 2, 3, 4, 5], 6) will return [5, 8] because 1 + 5 and 2 + 4 are also 6.
    Otherwise, it would just return a single product or 0 if none matches.
    """
    product = []
    for i, num1 in enumerate(num_list):
        for j, num2 in enumerate(num_list[i + 1:]):
            if num1 + num2 == goal:
                product.append(num1 * num2)
    if len(product) == 1:
        product = product[0]
    if not product:
        product = 0
    return product


class UpCounter:
    """
    This class initialises a counter from 0, receives a step size and increases the counter when update() is called.
    If no step size is provided, default value is 1. count() works as return the counter value.
    """

    def __init__(self, step_size=1):
        self.counter = 0
        self.step_size = step_size

    def count(self):
        return self.counter

    def update(self):
        self.counter += self.step_size


class DownCounter(UpCounter):
    """
    This class inherits from UpCounter, it does decrement instead in the update().
    """

    def update(self):
        self.counter -= self.step_size
