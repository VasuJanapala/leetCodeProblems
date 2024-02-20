from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        listNums = nums
        n = len(listNums)
        newList = list(range(0,n+1))
        # print(newList)
        for i in newList:
            if i in listNums:
                pass
            else:
                print(i)
        print(len(listNums))

if __name__ == "__main__":
    print("Missing number")
    mn = Solution()
    mn.missingNumber([0,3,1])