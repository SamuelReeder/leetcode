class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        stack = []

        opening = ['(', '{', '[']
        closing = [')','}', ']']
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                try: 
                    temp = stack.pop()
                except:
                    return False
                if opening.index(temp) != closing.index(i):
                    return False

        return len(stack) == 0
