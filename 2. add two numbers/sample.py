class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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
    
    def addTwoNumbers(self, l1, l2):
        len_l1 = 0
        len_l2 = 0
        itr = l1
        while itr:
            len_l1 +=1
            itr = itr.next
        itr = l2
        while itr:
            len_l2 +=1
            itr = itr.next

        if len_l1 == len_l2:
            l3 = Solution.calculation(l1, l2, len_l1, len_l2)           

        elif len_l1 > len_l2:
            while (len_l1 > len_l2):
                itr = l2
                while itr.next is not None:
                    itr = itr.next
                itr.next = ListNode(0, itr.next)
                len_l2 += 1 
            l3 = Solution.calculation(l1, l2, len_l1, len_l2)

        elif len_l1 < len_l2:
            while (len_l2 > len_l1):
                itr = l1
                while itr.next:
                    itr = itr.next
                itr.next = ListNode(0, itr.next)
                len_l1+=1
            l3 = Solution.calculation(l1, l2, len_l1, len_l2)
        return(l3)

l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

sol = Solution()

result = sol.addTwoNumbers(l1, l2)

# Printing the result
while result:
    print(result.val, end=" ")
    result = result.next
