class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # here I have created the dictionary to store the tuples with its length and the string respective to that string
        d = {}
        pos = 0
        for value1 in s:
            # print(value1)
            str1 = ''
            str1 += value1
            s2 = s[pos+1:]
            # print("value1: ",value1)
            for value2 in s2:
                # print("value2: ",value2)
                str1 += value2
                if value2 in str1 or (len(str1) == len(s)):
                    d[value1+str(pos)] = (len(str1), str1)
                    break
                # str1 += value2
            pos +=1
        max_value = max(val[0] for val in d.values())
        print(max_value)


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb" # yet to test it
    sol.lengthOfLongestSubstring(s)
    # print(s[-1])