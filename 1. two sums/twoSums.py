from typing import List
import json

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x = nums[i] + nums[j]
                if x == target:
                    return [i, j]
        return []

if __name__ == "__main__":

    # object creation
    solution = Solution()

    with open('twoSumsinputFile.json', 'r') as openJsonFile:
        data = json.load(openJsonFile)

    output = {}
    for (key_1, value), (key_2, target) in zip(data['values'].items(), data['target'].items()):
        output[key_1 + '_' + key_2] = {
            key_1 : value,
            key_2 : target,
            'indices': solution.twoSum(value, target)
        }

    with open('twoSumsOutputFile.json', 'w') as output_file:
        json.dump(output, output_file, indent=4)
    
