class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(reverse=True, key=lambda x: x[1])

        cnt = res = 0
        for num, units in boxTypes:
            
            tmp = truckSize - cnt
            if tmp < num:
                res += (tmp * units)
                break

            cnt += num
            res += (units * num)

        return res 
