# Lab 2

### function 1:

Analyze the following function with respect to number

```python
def function1(number):
    total = 0                   # 1

    for i in range(number):     # n + 1

        x = i + 1               # 2n
        total += x * x          # 2n

    return total                # 1
```

$T(n) = 1 + n + 1 + 2n + 2n + 1$

$= 5n + 3$

constants are to be ignored so $T(n) = O(n)$

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6  # 6 operators
```

$T(n) = 6$

constants are to be ignored so $T(n) = O(1)$

### function 3:

Analyze the following with respect to the length of the list. Note that the function call len() which returns the length
of the list is constant (O(1)) with respect to the length of the list.

```python

def function3(list):
    n = len(list)                           # 2
    for i in range(n - 1):                  # (n - 1) + 2 = n +１
        for j in range(n - 1 - i):          # 0.5n^2 + 2.5n - 3
            if (list[j] > list[j + 1]):     # 2 * (0.5n^2 - 0.5n) = n^2 - n
                tmp = list[j]               # 0.5n^2 - 0.5n
                list[j] = list[j + 1]       # 2 * (0.5n^2 - 0.5n) = n^2 - n
                list[j + 1] = tmp           # 2 * (0.5n^2 - 0.5n) = n^2 - n

```
		
![image](https://github.com/seneca-dsa456/labs-kchu30/assets/61229735/1b53e668-a181-4cb0-8f5c-0ed942ede35d) ![image](https://github.com/seneca-dsa456/labs-kchu30/assets/61229735/6fffc668-6706-42f4-b47c-9c7757b88cd3)


$T(n) = 2 + ( n + 1) + 0.5n^2 + 2.5n - 3 + 7 * (0.5n^2 - 0.5n)$
$= 4n^2$

so $T(n) = O(n^2)$


### function 4:

Analyze the following function with respect to number

```python
def function4(number): 
    total = 1                       # 1 
    for i in range(1, number):      # (n - 1) + 1
        total *= i + 1              # 2n
    return total                    # 1
```

$T(n) = 1 + n + 2n + 1$
$= 3n + 2$

constants are ignored so $T(n) = O(n)$

## In class portion

### Group members

List the members of your group member below:

	* Name 
	* ex. Samuel Vimes
	* ...

### Timing Data

Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member     | Timing for fibonacci   | Timing for sum_to_number | 
|-----------------|------------------------|--------------------------|
| Alex Chu        | 7.399999987001138e-06  | 1.1200491030000705       |
| Kenneth Reforma | 8.199999996350016e-06  | 0.003946981000041205     |
| Hao Yang        | 3.6977515339999627     | 0.7115866140006801       |
| Dan Zhang       | 4.300000000512227e-06  | 0.7701728920001187       | 
| David She       | 2.947257825000001      | 0.9835719920000017       |
| David Nguyen    | 5.900000004999129e-06  | 0.8024703360000061       |

### Summary

| function      | fastest               | slowest            | difference               
|---------------|-----------------------|--------------------|--------------------------|
| sum_to_number | 0.003946981000041205  | 1.1200491030000705 | 1.116102122000029295     |
| fibonacci     | 4.300000000512227e-06 | 2.947257825000001  | 2.947253525000000487773  |

### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax?
A difference in approach? Write down your observations.

## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and
   slowest versions of code?
> Most of us have quite similar or identical time for fibonacci because the structure are very similar, apart from 1 solution was using recursion which is the slowest. However, sum_to_number has big differences. The reason behind is, some of us managed to refine the function to a more efficient algorithm and make it an O(n) or O(nlogn) to avoid the nested loop. Therefore, it is essential to reduce the complexity of codes whenever it is possible, especially when the code is being used over and over to reduce the load (resource, memory) and time.

2. Was there a difference in terms of usage of space resource? Did one algorithm use more/less space (memory)?
> For the fibonacci function if we write in a way using recursion, it would dramatically increase the usage of space resource as well as time resource. Therefore, to avoid stack overflow, I rewrote my code without using recursion. Recursion must be well planned of using a base case so that it wouldn't fall into an infinite loop or drain all the memory. 

3. What sort of conclusions can you draw based on your observations?
> As a conclusion combining my opinions above, it is easy to write a piece of code functioning, but it is difficult to write a piece code efficient. So here we are to learn how to analyse the code and learn more about algorithms. As said in class, we barely say best case but average case and worse case, hence we should plan for a better worse case. E.g. a O(n), O(logn), O(nlogn) is always better than $O(n^2)$, $O(n^3)$ etc.  


