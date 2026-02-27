class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = res = 0
        hm = defaultdict(int)
        hm[0] = 1
        for i in nums:
            # we have a prefix from start
            prefix += i

            # at current index, if theres a prefix s.t. total - k == prefix, we have total - prefix = k
            if prefix - k in hm:
                res += hm[prefix - k]

            hm[prefix] += 1
        
        return res

