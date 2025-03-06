def f(n):
    count = 1
    for i in range(0,n):
        for j in range(0,n-i):
            print(count, " i: ", i, " j ", j)
            count += 1
        print("\n")

f(2)

def lonelyinteger(a):
    # Initialize result to 0
    result = 0
    # XOR every element in the array to the result
    for num in a:
        result ^= num
    # Return the result
    return result
print(lonelyinteger([1,2,2,1]))