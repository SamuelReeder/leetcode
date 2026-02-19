class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def helper(i, comb, s):
            if s == target:
                res.append(list(comb))
                return
            elif s > target or i == len(candidates):
                return

            # include i or not
            comb.append(candidates[i])
            helper(i, comb, s + candidates[i])

            comb.pop()
            helper(i + 1, comb, s)

        helper(0, [], 0)

        return res
