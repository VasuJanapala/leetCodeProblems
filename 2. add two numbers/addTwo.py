import json

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # creating the lengths of each linked list by travesing
        len_l1 = 0  #length of list L1
        len_l2 = 0  #length of list L2

        # traversing the list 1
        itr = l1
        while itr:
            len_l1 +=1
            itr = itr.next
        
        # traversing the list 1
        itr = l2
        while itr:
            len_l2 +=1
            itr = itr.next

        # if lengths are equal, we do not have to add extra zero nodes for the lists
        if len_l1 == len_l2:
            l3 = Solution.calculation(l1, l2, len_l1, len_l2) 

        # if lengths are unequal, in this case, the list L2 is less than list L1. In this case we must add extra nodes that matches the lenght of list L1         
        elif len_l1 > len_l2:
            while (len_l1 > len_l2):
                itr = l2
                while itr.next is not None:
                    itr = itr.next
                itr.next = ListNode(0, itr.next)
                len_l2 += 1                         # each time when I add the node, the length increases, so the respective length is incremented
            l3 = Solution.calculation(l1, l2, len_l1, len_l2)
        
        # if lengths are unequal, in this case, the list L1 is less than list L2. In this case we must add extra nodes that matches the lenght of list L2
        elif len_l1 < len_l2:
            while (len_l2 > len_l1):
                itr = l1
                while itr.next:
                    itr = itr.next
                itr.next = ListNode(0, itr.next)
                len_l1+=1                           # each time when I add the node, the length increases, so the respective length is incremented
            l3 = Solution.calculation(l1, l2, len_l1, len_l2)
        return l3
    
    # this method helps to perform the addition operation. Which brings the desired result.
    def calculation(l1, l2, len_l1, len_l2):
        l3 = None
        updated_list = []
        i, j, quo = 0, 0, 0
        while i < len_l1 or j < len_l2:
            add = l1.val + l2.val + quo
            updated_list.append(add%10)
            quo = add//10
            i += 1
            j += 1
            l1 = l1.next
            l2 = l2.next
        if quo!=0:
            updated_list.append(quo)
        updated_list = updated_list[::-1]
        for value in updated_list:
            if l3 is None:
                l3 = ListNode(value, None)
            else:
                node = ListNode(value, l3)
                l3 = node
        return l3

if __name__ == "__main__":
    sol = Solution()

    with open('addTwoInputFile.json', 'r') as file:
        data = json.load(file)
    # print(data)
    for keys in data:
        l1 = None
        l2 = None
        # print(keys)
        list_1 = data[keys]['list1']
        list_2 = data[keys]['list2']
        for i in list_1:
            l1 = ListNode(i, l1)
        for i in list_2:
            l2 = ListNode(i, l2)
        result = sol.addTwoNumbers(l1, l2)
        # Printing the result
        while result:
            print(result.val, end=" ")
            result = result.next
        print()
