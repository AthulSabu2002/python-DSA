from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, float('inf')
        
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = max(profit, p - min_price)
        
        
        return profit
    
    
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.maxProfit(prices = [10,1,5,6,7,1]))