class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        def helper(opened: int, close:int, s: str):
            if len(s) == 2*n:
                result.append(s)
                return
            
            if opened < n:
                helper(opened + 1, close, s + "(")

            if close < opened:
                helper(opened, close + 1, s + ")")


        if n == 1:
            return ["()"]
        
        helper(1, 0, "(")
        return result

    

       
