class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = dict()

        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in hm:
                return [i, hm[tmp]]
            hm[nums[i]] = i
                
    

