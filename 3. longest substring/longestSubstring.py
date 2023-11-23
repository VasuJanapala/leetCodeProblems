import json


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # here I have created the dictionary to store the tuples with its length and the string respective to that string
        d = {}
        pos = 0
        if s!='':
            for value1 in s:
                str1 = ''
                str1 += value1
                s2 = s[pos+1:]
                for value2 in s2:
                    if value2 in str1:
                        d[value1+str(pos)] = (len(str1), str1)
                        break
                    str1 += value2
                if len(str1) == len(s):
                    d[value1+str(pos)] = (len(str1), str1)
                    break
                else:
                    d[value1+str(pos)] = (len(str1), str1)
                pos +=1
            max_value = max(val[0] for val in d.values())
            return max_value
        elif s == '':
            return 0

if __name__ == "__main__":
    sol = Solution()
    output = {}
    file_open = open("longestInput.json", "r")
    data = json.load(file_open)
    for key, input in data.items():
        output[input] = sol.lengthOfLongestSubstring(input)

    with open("longestOutput.json", "w") as output_file:
        json.dump(output, output_file, indent = 4)
