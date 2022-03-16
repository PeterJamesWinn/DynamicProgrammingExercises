

def fibonacci(n, f_record={}):
    if n in f_record.keys(): return f_record[n]
    if n == 0: return 0
    if n == 1 or n == 2: return 1

   
    f_record[n] = fibonacci(n-1) + fibonacci(n-2)
    return f_record[n]

def fibonacci_list(n, f_record=[]):
    try: return f_record[n]
    except: 
        for i in range(2,n): f_record[i] = -1
    if n == 0: return 0
    if n == 1 or n == 2: return 1

   
    f_record[n] = fibonacci(n-1) + fibonacci(n-2)
    return f_record[n]


class fibonacci_recursive_memo_class:
    def __init__(self):
        self.memo = {}
    
    def calculate_fibonacci(self, n):
       if n in self.memo.keys(): return self.memo[n]
       if n == 0: return 0
       if n <= 2 and n > 0: return 1
       self.memo[n] = (self.calculate_fibonacci(n-1) + self.calculate_fibonacci(n-2))
       return self.memo[n]

for n in range(0,10):
    print(n, fibonacci_list(n))


for n in range(0,10):
    print(n, fibonacci(n))


