class Solution:
    def __init__(self):    
        self.memo = {1: 1, 2: 2}
    
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return self.memo[n]


if __name__ == "__main__":
    obj = Solution()
    
    print(obj.climbStairs(n = 3))