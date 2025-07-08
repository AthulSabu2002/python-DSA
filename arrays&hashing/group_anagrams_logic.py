from typing import List

class Solution:
    def count_characters(self, word: str) -> List[int]:
        count = [0] * 26
        
        for ch in word:
            index = ord(ch) - ord('a')
            count[index] += 1
        
        return count
    
    def are_same_signatures(self, sig1, sig2):
        for i in range(26):
            if (sig1[i] != sig2[i]):
                return False
        
        return True
    
    def group_anagrams(self, lst: List[str]) -> List[List[str]]:
        
        signatures = []
        groups = []
        
        for word in lst:
            current_sign = self.count_characters(word)
            
            placed = False
            for i in range(len(signatures)):
                if self.are_same_signatures(current_sign, signatures[i]):
                    groups[i].append(word)
                    placed = True
                    break
            if not placed:
                groups.append([word])
                signatures.append(current_sign)
        
        
        return groups

if __name__ == "__main__":
    obj = Solution()
    
    print(obj.group_anagrams(["act","pots","tops","cat","stop","hat"]))