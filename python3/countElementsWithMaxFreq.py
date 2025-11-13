class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        hm = {}
        freq = {}

        m = 0
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

            m = max(hm[num], m)
            if hm[num] in freq:
                freq[hm[num]] += hm[num]
            else: 
                freq[hm[num]] = hm[num]

        return freq[m]
