class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        new_arr = sorted(arr)
        ranks = {}
        rank = 1
        for v in new_arr:
            if v not in ranks:
                ranks[v] = rank
                rank += 1
        
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]

        return arr
            

