class Solution:
    def myAtoi(self, s: str) -> int:

        if len(s) == 0:
            return 0

        s = s.strip()

        sign = 1

        if len(s) > 1:
            if s[0] == '-':
                sign = -1
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]

        maximum = 2**31 - 1
        minimum = -1 * 2**31

        num = 0
        for c in s:

            if c.isdigit():
                digit = int(c)
            else:
                break

            if (maximum - digit) / 10 < num:
                if sign == -1:
                    return minimum
                return maximum

            num *= 10
            num += digit
        
        return sign * num
        
