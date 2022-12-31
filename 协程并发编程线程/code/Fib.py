
class Fab(object):
 
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()
 
for n in Fab(5):
    print(n)
# =================================== recursion(Top-Down) --- stackful coroutine

def recur_fibo(n):
   """递归函数
   输出斐波那契数列"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
print(recur_fibo(5))

# =================================== loop(Bottom-Up) --- stackful coroutine

List = [1,1]
def loop_fib(n):
    for i in range(1,n+1):
        if i==1 or i == 2:
            pass
        else:
            List.append(List[i-2]+List[i-3])
loop_fib(5)
print(List)



# ====================================== yield --- stackless coroutine
def fib_yield(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b 
        n = n + 1

for n in fib_yield(5): 
    print(n)



