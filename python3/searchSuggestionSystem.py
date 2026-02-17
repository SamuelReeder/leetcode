# improvement: use bisect to find inserion point

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()

        hm = dict()
        for i in range(len(searchWord)):
            hm[searchWord[:i + 1]] = []

        for i in products:
            for j in range(len(i)):
                tmp = i[:j + 1]
                if tmp not in hm:
                    break
                else:
                    hm[tmp].append(i)
        
        res = []
        for i in range(len(searchWord)):
            res.append(hm[searchWord[:i + 1]][:3])

        return res
