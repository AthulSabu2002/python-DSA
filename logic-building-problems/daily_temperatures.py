from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
            
        return res
    
    
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.dailyTemperatures([30,38,30,36,35,40,28]))