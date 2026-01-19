class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        running, remaining, res, idx = 0, 0, -1, -1
        
        for i in range(1, len(customers) + 1):
            remaining += customers[i - 1]
            
            num = min(4, remaining)
            remaining -= num
            
            running += num * boardingCost - runningCost
            
            if running > res:
                res = running
                idx = i
        
        i = len(customers) + 1
        while remaining > 0:
            num = min(4, remaining)
            remaining -= num
            
            running += num * boardingCost - runningCost
            
            if running > res:
                res = running
                idx = i
            i += 1

        return idx if res > 0 else -1
