class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")

        res = []
        for word in words:
            
            w = word.lower()

            for row in [first, second, third]:
                valid = True
                for c in w:
                    if c not in row:
                        valid = False
                        break

                if valid:
                    res.append(word)
                    break
            
        return res
                


