class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        string = "123456789"
        
        res = []
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):    
                num = int(string[i:j])
                if low <= num and high >= num:
                    res.append(num)
        
        return sorted(res)
    
