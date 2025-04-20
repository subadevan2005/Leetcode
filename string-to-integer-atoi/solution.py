class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        res = 0
        sign = 1
        s = s.lstrip()
        
        if not s:
            return 0

        # sign determination
        if s[0] == "+" or s[0] == "-":
            sign = -1 if s[0] == "-" else 1
            i += 1

        # finding digits in the string
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i]) 
            i += 1

        res *= sign
        # limiting the number within 32bit
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res
