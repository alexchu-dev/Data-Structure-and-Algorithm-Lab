# Analysis and Reflection for Lab 1

## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
    if number == 0:             # 1 (base case)
        return 1                # 0
    elif number == 1:           # 1 (base case)
        return value            # 0
    else:
        return value * function1(value, number - 1) # 2 + T(n - 1)
```

$T(n) = 1 + 1 + 2 + T(n - 1)$

$T(n) = 4 + T(n - 1)$

$T(n) = 4 + (4 + T(n - 2)) = 4 * 2 + T(n - 2)$

$T(n) = 4 + (4 + (4 + T(n - 3))) = 4 * 3 + T(n - 3) $

$T(n) = 4 * k + T(n - k)$ where $T(0)$ = 1op, thus $k = n - 1$

$T(n) = 4(n - 1) + T(1) = 4n - 4 + 2$

$T(n) = 4n - 2$

Thus, $T(n)$ is $O(n)$



## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring, left, right):
    if left >= right :                  # 1 (base case)
            return True                 # 0
    else:
        if mystring[left] != mystring[right]:   # 3 (base case)
                return False            # 0
        else:
                return recursive_function2(mystring, left + 1, right - 1)   # T(n - 2)

def function2(mystring):
        return recursive_function2(mystring, 0, len(mystring)-1)

```

The worst scenario is the recursion (1 + 3 + T(n - 2)) towards the base case plus the last few operators 1 + 3 + 1.

Let's find out the T(n).

$T(n) = 4 + T(n - 2)$

$T(n) = 4 + (4 + T(n - 4)) = 4 * 2 + T(n - 2 * 2)$

$T(n) = 4 + 4 + 4 + T(n - 6)) = 4 * 3 + T(n - 2 * 3)$

$T(n) = 4 * k + T(n - 2 * k)$, thus $n - 2k = 0$, $k = {n \over 2}$

$T(n) = 2n + T(0) = 2n + 1 = O(n)$



### function 3 (optional challenge):

Analyze the following function with respect to number


```python
def function3(value, number):
    if number == 0:                 # 1
            return 1                # 0
    elif number == 1:               # 1
            return value            # 0
    else:
            half = number // 2              # 2
            result = function3(value, half) # 1 + (T(n/2)
            if number % 2 == 0:             # 2
                    return result * result  # 0
            else:
                    return value * result * result  # 2

```
T(n) = ... if n == 0 : 1 ... if $n == 1 : 2

otherwise: $7 + T([n/2])$ (My count is 9 + T(n/2) but following the demo in lab now its 7)

$T(n) = 7 + T({n\over 2})$

$T(n) = 7 + 7 + T({n\over 4})$

$T(n) = 7 + 7 + 7 + T({n\over 8}) = 7 * 3 + T({n\over 2^3})$

$T(n) = 7 * k + T({n\over 2^k})$, thus ${n\over 2^k} = 1$, $k = \log_{2}n$

$T(n) = 7\log_{2}n + T(1) = 7\log_{2}n + 2$

$T(n) = O(\log_{2}n)$]



## Part C reflection

Answer the following questions

1. Describe how to approach writing recursive functions, what steps do you take?
> To start writing resursive functions, first of all I think about the possible base cases. After addressing both success and unsuccessful base case which the loop ends at, I can start thinking about the recursive part. The recursive part isn't too difficult, but the most important thing is I have to stop the loop from being infinite. I have the exact problem when I was writing my recursive binary search. I tried to write four arguments and set two of them default as 0. Then, when I assigned the true default value to one of the pointer, I got infinite loop. Therefore, I correct my code to this:
>{ if high == 0 and low != 0: } which I added the extra condition of low not equal to zero which can avoid when hitting the base case and both low and high are zero it goes infinite.

2. Describe the process of analyzing recursive functions.  How does it differ from analyzing non-recursive functions?  How is it the same? 
> Analyzing recursive functions takes extra care of how we stack up the loop. It all starts from finding the base cases first, then we can start thinking about how the program actually call the recursion and what would the "n" be, and so that the equation we write would make sense. The style we write the equation is different as T(n) would always include the recursive ones such as T(n - 1) or T(n/2) etc inside.
> The style we analyze both of these recursive and non-recursive are actually similar, which the foundation of doing these analysis are the same, just the contents and how it nested are different. In terms of complexity, Non-recursive could be complicated as well with nested structures. In general, recursive functions have to take care of the base cases so as how we analyze them.
