# copy over your code from lab 1 to this file.
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

