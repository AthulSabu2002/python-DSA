class Solution:
    def knapsackRec(self, W, val, wt, n):
        if n == 0 or W == 0:
            return 0

        pick = 0

        if wt[n - 1] <= W:
            pick = val[n - 1] + self.knapsackRec(W - wt[n - 1], val, wt, n - 1)
        
        notPick = self.knapsackRec(W, val, wt, n - 1)
        
        return max(pick, notPick)

    def knapsack(self, W, val, wt):
        n = len(val)
        return self.knapsackRec(W, val, wt, n)


if __name__ == "__main__":
    obj = Solution()
    
    print(obj.knapsack(W= 5, val= [10, 40, 30, 50], wt= [5, 4, 2, 3] ))