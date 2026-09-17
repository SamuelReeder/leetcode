class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        threshold = len(arr) // 4

        last = arr[0]
        cnt = 1
        for num in arr[1:]:
            if last == num:
                cnt += 1
            else:
                last = num
                cnt = 1

            if cnt > threshold:
                return num

        return last
