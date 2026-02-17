class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letters = []
        digits = []

        for log in logs:
            
            i = log.find(" ")

            if log[i + 1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        print(letters)
        print(digits) 

        def f(x):
            i = x.find(" ")
            return (x[i+1:], x[:i])

        letters.sort(key=f)

        return letters + digits
