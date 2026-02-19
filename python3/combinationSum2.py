class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)

        res = []    

        def helper(i, comb, s):
            if s == target:
                res.append(list(comb))
            if s >= target or i == len(candidates): 
                return 

            
            comb.append(candidates[i])
            helper(i + 1, comb, s + candidates[i])
            comb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
                
            helper(i + 1, comb, s)

        helper(0, [], 0)

        return res

        
