class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dic = {}
        for i in magazine:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i in ransomNote:
            if i not in dic or dic[i] == 0:
                return False
            dic[i] -= 1
        
        return True
