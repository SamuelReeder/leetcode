class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = (10**9 + 7)

        # for each arr[i], for how many subarrays is it the min
        # all the subarrays including it with no smaller element

        left = []

        stack = []
        for i in range(n):

            while stack and stack[-1][1] >= arr[i]:
                stack.pop()

            left.append(stack[-1][0] + 1 if stack else 0)
            stack.append((i, arr[i]))

        s = 0
        stack = []
        for i in range(n - 1, -1, -1):

            while stack and stack[-1][1] > arr[i]:
                stack.pop()

            tmp = stack[-1][0] - 1 if stack else n - 1
            total = (i - left[i] + 1) * (tmp - i + 1) * arr[i]
            s = (s + total) % MOD

            stack.append((i, arr[i]))

        return s


        

