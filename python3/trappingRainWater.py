class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        max_left = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                max_left[i] = height[i]
                continue
                
            max_left[i] = max(max_left[i-1], height[i])

        max_right = [0] * len(height)
        for i in range(len(height) - 1, -1 , -1):
            if i == len(height) - 1:
                max_right[i] = height[i]
                continue
                
            max_right[i] = max(max_right[i+1], height[i])

        for i in range(1, len(height) - 1):
            temp = min(max_left[i-1], max_right[i+1]) - height[i]
            total += temp if temp > 0 else 0

        
        return total

                    

