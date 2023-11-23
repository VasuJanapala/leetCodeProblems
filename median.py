from typing import List
import json

class Median:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        listNumber_1 = nums1
        listNumber_2 = nums2
        listNumbers = listNumber_1 + listNumber_2
        listNumbers = sorted(listNumbers)
        length_list = len(listNumbers)
        if (length_list%2==0):
            midValue = length_list//2
            median = (listNumbers[midValue-1] + listNumbers[midValue])/2
            return median
        elif (length_list%2!=0): 
            midValue = length_list//2
            median = listNumbers[midValue]
            return median

    

if __name__ == "__main__":

    nums1 = [1, 2]
    nums2 = [3, 4]
    median = Median()

    outputs = {}

    with open ("twoArrays.json","r") as fileOpen:
        data = json.load(fileOpen)
    for key, values in data.items():
        outputs[key+' median is'] = median.findMedianSortedArrays(values['nums1'], values['nums2'])
    with open ("twoArrysOutput.json", "w") as file:
        json.dump(outputs, file, indent=4)

    


    
    
