class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # some sort of recursion
        # maybe we keep track of the open parenthesis
        
        res = []
        def helper(s, cnt):
            if len(s) == n * 2:
                res.append(s)
                return

            if cnt < n:
                helper(s + "(", cnt + 1)
            
            if cnt > len(s) - cnt:
                helper(s + ")", cnt)
            
        helper("", 0)

        return res
        
