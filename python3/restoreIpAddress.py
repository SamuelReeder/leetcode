class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # for each starting point, we try to construct the first integer and continue to each starting point of next
        # early return if integer doesnt work
        # if we get to the last char, add to list

        res = []
        def helper(ls, i):
            if len(ls) == 4:
                if i == len(s):
                    res.append('.'.join(map(str, ls)))
                return

            for j in range(1, 4):
                if j + i > len(s):
                    break

                tmp = int(s[i:i+j])

                if not 0 <= tmp <= 255:
                    break

                ls.append(tmp)
                helper(ls, i+j)
                ls.pop()

                if j == 1 and tmp == 0:
                    break

        helper([], 0)
        return res


            
