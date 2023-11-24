import json

class LPalindrome:
    def longestPalindrome(self, s: str) -> str:
        stringIs = s
        storage = {}
        pos = 0
        if stringIs == stringIs[::-1]:
            return stringIs
        else:
            for i in stringIs:
                stringIsSub = stringIs[pos+1:]
                dummyString = i
                for j in stringIsSub:
                    dummyString += j
                    if j==i and dummyString == dummyString[::-1]:
                        storage[dummyString] = len(dummyString)
                pos += 1
            # print(storage)
            if storage:
                max_key = max(storage, key = storage.get)
                return max_key
            else:
                return stringIs[0]            

if __name__ == "__main__":
    longPalin = LPalindrome()
    s = "babad"
    s2 = "cbbbbd"
    s3 = "ccc"
    s4 = "xaabacxcabaaxcabaax"
    s5 = "ac"

    outputs = {}

    with open("longPalindromeInputs.json", "r") as readInputs:
        data = json.load(readInputs)
    for key, value in data.items():
        outputs[key + "_output"] = longPalin.longestPalindrome(value)
    with open("longPalindromeOutputs.json","w") as writeOutputs:
        json.dump(outputs, writeOutputs, indent = 4)