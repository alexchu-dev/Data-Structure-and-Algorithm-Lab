#
# Author: 
# Student Number:
#
# Place the code for your lab 3 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#
import random


def factorial(number):
    rc = 1
    if number > 1:
        rc = number * factorial(number - 1)
    return rc


def linear_search(my_list, key, index=0):
    """Added one argument in here, to make use of optional argument (default value).
    Otherwise, it would need two functions to work."""
    if index >= len(my_list):
        return -1  # Base case/ Worst case when result no match
    elif my_list[index] == key:
        return index  # Case when key matches
    else:
        return linear_search(my_list, key, index + 1)  # Recursive call and passing increased index.


# my_list = random.sample(range(1, 100), 10)
# print(f"Unsorted List: {my_list}")
# print(linear_search(my_list, 10))


def binary_search(my_list, key, low=0, high=0):
    """
    # This first condition is to assign the initial index at the first time when argument default as 0.
    To avoid infinite loop, I added low != 0 so that when the case both low and high hits 0, it will not
    reassign high again.
    """
    if high == 0 and low != 0:
        high = len(my_list) - 1
    if low <= high:
        mid = (low + high) // 2
        if my_list[mid] == key:
            return mid
        elif my_list[mid] < key:
            return binary_search(my_list, key, mid + 1, high)
        else:
            return binary_search(my_list, key, low, mid - 1)

    else:
        return -1


