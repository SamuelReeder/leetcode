class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current = highest
        for i in range(len(gain)):
            current += gain[i]
            highest = max(current, highest)
        
        return highest
        
