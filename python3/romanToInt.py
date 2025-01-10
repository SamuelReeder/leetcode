class Solution:
    def romanToInt(self, s: str) -> int:
        

        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        valid_pairs = {
            ('I', 'V'), ('I', 'X'),
            ('X', 'L'), ('X', 'C'),
            ('C', 'D'), ('C', 'M') 
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            if i < n - 1 and (s[i], s[i + 1]) in valid_pairs:
                total -= roman_values[s[i]]
            else:
                total += roman_values[s[i]]
        
        return total

