class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # look for max in citations where there are max values greater than it 
        
        citations.sort(reverse=True)

        total = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                total = i + 1
            else:
                break
        return total
