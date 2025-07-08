class Solution:
    def isValid(self, s: str) -> bool:
        lst = list(s)
        print(lst)
        dictK = {'{': '}', '(': ')', '[': ']'}
        openP = ['[', '{', '(']
        stk = []
        for ch in lst:
            if ch in openP:
                stk.append(dictK[ch])
            else:
                
                if len(stk) > 0 and stk[-1] == ch:
                    stk.pop()
                else:
                    return False
        
        if len(stk) > 0:
            return False
    
        return True
        
        
        
if __name__ == "__main__":
    obj = Solution()
    s = "()()"
    
    print(obj.isValid(s))