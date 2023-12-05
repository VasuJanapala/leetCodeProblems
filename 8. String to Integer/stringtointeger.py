import json

class StringToInteger:
    def myAtoi(self, s: str) -> int:

        if s == "":
            return 0
        # to remove leading whitespace
        s = s.lstrip()
        if s == "":
            return 0
        sign = 1
        result = 0

        INT_MAX = 2**31-1
        INT_MIN = -2**31

        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        result = sign * result
        result = max(min(result, INT_MAX),INT_MIN)
        print(result)


if __name__ == '__main__':
    strtoint = StringToInteger()
    # s = "words and 987"
    # s = "4193 with words"
    s = "   -42"
    # s = "abc+42"
    strtoint.myAtoi(s)