

import timeit
import numpy as np

def fibonacci_recursive(n): # this is a top down approach, i.e. start and n and create calls for every fibonacci number before n
    if n == 0: return 0
    if n <= 2 and n > 0: return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_recursive_memo(n, memo = {}):  # this is a top down approach, i.e. start and n and create calls for every fibonacci number before n
    if n in memo.keys(): return memo[n]   # check to see if this value has been calculated previously; if so it is saved in memo. 
    if n == 0: return 0
    if n <= 2 and n > 0: return 1
    memo[n]= fibonacci_recursive_memo(n-1) + fibonacci_recursive_memo(n-2)   # if new value, calculate it and store to memo. 
    return memo[n]

class fibonacci_recursive_memo_class:
    def __init__(self):
        self.memo = {}
    
    def calculate_fibonacci(self, n):
       if n in self.memo.keys(): return self.memo[n]
       if n == 0: return 0
       if n <= 2 and n > 0: return 1
       self.memo[n] = (self.calculate_fibonacci(n-1) + self.calculate_fibonacci(n-2))
       return self.memo[n]

    

def fibonacci_iterative(n):  # bottom up approach. calculate each fibonacci in ascending order until we get to the desired value. 
    if n == 0: return 0
    if n <= 2 and n > 0: return 1
    if n > 2:
        a = 1
        b = 1
        for n in range(3,n+1):
            c = a + b
            a = b 
            b = c 
        return c  


def fibonacci_iterative_table(n):  # bottom up approach. calculate each fibonacci in ascending order until we get to the desired value.
    results_table=np.zeros(n+1)
    if n == 0: 
        return results_table[0]
    results_table[1] = 1
    if n == 1: 
        return results_table[1]
    results_table[2] = 1
    if n == 2: 
        return results_table[2]
    if n > 2:
        #results_table[2] = 1
        for i in range(3,n+1):            
            results_table[i] = results_table[i-1] + results_table[i-2]  
    return results_table[n]

def fibonacci_iterative_table2(n):  # bottom up approach. calculate each fibonacci in ascending order until we get to the desired value.
    results_table=np.zeros(n+1)
    if n == 0: return results_table[0]
    results_table[1:3] = 1
    if n <= 2 and n > 0: 
        return results_table[1]
    if n > 2:
        #results_table[3] = 1
        for n in range(2,n):
            results_table[n+1] = results_table[n+1] + results_table[n] + results_table[n-1]    
    return results_table[n+1]

## Testing Code
print("fibonacci_recursive no memo (painfully slow:")
for i in range(7):    
    print("Fibonacci number, {}: {}".format(i, fibonacci_recursive(i)))

print("fibonacci_iterative_table2, start:")
for i in range(0,20):    
    print("Fibonacci number, {}: {}".format(i, fibonacci_iterative_table2(i)))
print("fibonacci_iterative_table2, finish:")

print("fibonacci_iterative_table, start:")
for i in range(0,20):    
    print("Fibonacci number, {}: {}".format(i, fibonacci_iterative_table(i)))
print("fibonacci_iterative_table, finish:") 

fibonacci = fibonacci_recursive_memo_class()  # instantiate a class
for i in range(1,20):
    print(fibonacci.calculate_fibonacci(i))
#
for i in range(1,20):
    print(fibonacci_recursive_memo(i))
#
for i in range(1,20):
    print(fibonacci_iterative(i))

print("recursive  no memo - 8 Fibonacci numbers only - the others are all 40 ", timeit.timeit('fibonacci_recursive(8)', globals=globals(), number=100)) # this is really so slow that not worth comparing with others. 
fibonacci = fibonacci_recursive_memo_class()   # instantiate a class
print("class  recursive memo", timeit.timeit('fibonacci.calculate_fibonacci(40)', globals=globals(), number=100))
print(" recursive memo", timeit.timeit('fibonacci_recursive_memo(40)', globals=globals(), number=100))
print("iterative", timeit.timeit('fibonacci_iterative(40)', globals=globals(), number = 100 ))
print("iterative table", timeit.timeit('fibonacci_iterative_table(40)', globals=globals(), number = 100 ))
print("iterative table2", timeit.timeit('fibonacci_iterative_table2(40)', globals=globals(), number = 100 ))

print("Repeat timings to see any runtime variation:")
print("class  recursive memo", timeit.timeit('fibonacci.calculate_fibonacci(40)', globals=globals(), number=100))
print(" recursive memo", timeit.timeit('fibonacci_recursive_memo(40)', globals=globals(), number=100))
print("iterative", timeit.timeit('fibonacci_iterative(40)', globals=globals(), number = 100 ))
print("iterative table", timeit.timeit('fibonacci_iterative_table(40)', globals=globals(), number = 100 ))
print("iterative table2", timeit.timeit('fibonacci_iterative_table2(40)', globals=globals(), number = 100 ))
