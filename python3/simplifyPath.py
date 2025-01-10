class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []

        for i in arr:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
        
        s = ""
        for i in stack:
            s += f"/{i}"

        if len(stack) == 0:
            s = "/"

        return s            

        
