from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        res = 0
        nums = []
        operators = ['+', '-', '/', '*']
        for i in range(len(tokens)):
            if tokens[i] in operators:
                if tokens[i] == '+':
                    res = nums[-2] + nums[-1]
                    nums.pop()
                    nums.pop()
                    nums.append(res)
                elif tokens[i] == '*':
                    res = nums[-2] * nums[-1]
                    nums.pop()
                    nums.pop()
                    nums.append(res)
                elif tokens[i] == '/':
                    res = int(nums[-2] / nums[-1])
                    nums.pop()
                    nums.pop()
                    nums.append(res)
                elif tokens[i] == '-':
                    res = nums[-2] - nums[-1]
                    nums.pop()
                    nums.pop()
                    nums.append(res)
            else:
                nums.append(int(tokens[i]))
                
        return res
 
    
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))