import time

class Solution():
    def __init__(self):
        self.memo = {1: 1, 2: 1}
    
    def fib(self, n):
        if n <= 0:
            return 0
        
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]
    

if __name__ == "__main__":
    obj = Solution()
    
    start = time.perf_counter()
    
    result = obj.fib(7000)
    
    end = time.perf_counter()
    
    print("Result:", result)
    print(f"Time taken: {end - start:.6f} seconds")