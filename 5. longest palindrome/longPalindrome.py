
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
    print(longPalin.longestPalindrome(s5))