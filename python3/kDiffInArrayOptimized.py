class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        actual_pairs = set()
        
        for num in nums:
            if num - k in seen:
                actual_pairs.add(num - k)
            if num + k in seen:
                actual_pairs.add(num)
            seen.add(num)
            
        return len(actual_pairs)
