class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = self.getDictionary(s)
        dictt = self.getDictionary(t)
        
        for key in dicts:
            if key not in dictt.keys() or dicts[key] != dictt[key]:
                return False
        
        return True 
    
    def getDictionary(self, k):
        dict = {}
        for c in k:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        
        return dict   


if __name__ == "__main__":
    obj = Solution()
    print(obj.isAnagram("racecar", "carrace"))