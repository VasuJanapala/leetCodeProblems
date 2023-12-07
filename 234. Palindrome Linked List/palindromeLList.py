import json

class ListNode:
    def __init__(self, val = 0, next = None):
        self.value = val
        self.next = next

class PalindromeLinkedList:
    def isPalindrome(self, head)->bool:
        # def middle(node):
        #     slow = fast = node
        #     while fast and fast.next:
        #         slow = slow.next
        #         fast = fast.next
        #     return slow
        
        # def reverse_second(node):
        #     prev = None
        #     current = node
        #     while current:
        #         next_node = current.next
        #         current.next = prev
        #         prev = current
        #         current = next_node
        #     return prev
        
        # middle_node = middle(head)
        # reversed_second_half = reverse_second(middle_node)

        # while reversed_second_half:
        #     if head.value!=reversed_second_half.value:
        #         return False
        #     head = head.next
        #     reversed_second_half = reversed_second_half.next
        # return True
        itr = head
        # record_list = 0
        back_up_value = 0

        record_list = []
        while itr!=None:
            
            # record_list = record_list * 10 + itr.value
            itr_last = itr.value
            record_list.append(itr.value)
            itr = itr.next
            
        length = (len(record_list))
        if (length >=1 and length < 10**5):
            reversed_value = record_list[::-1]
            return(reversed_value == record_list)
        else:
            return False
        # print(itr_last)
        # itr = head
        # if itr.value == 0 and itr_last == 0:
        #     record_list = record_list//10
        
        # print(record_list)
        
        # reference_value = record_list
        # while(record_list!=0):
        #     rem = record_list%10
        #     record_list = record_list//10
        #     reversed_value = reversed_value * 10 + rem
        
        # print(reference_value == reversed_value)

if __name__ == '__main__':
    pll = PalindromeLinkedList()
    listNode = None
    

    with open("palindromLListInputFile.json", "r") as fread:
        data = json.load(fread)
    
    output = {}
    for key, value in data.items():
        for i in value:
            listNode = ListNode(i, listNode)
        output["output_" + key]  = pll.isPalindrome(listNode)
    
    with open("palindromeLListOutputFile.json", "w") as fwrite:
        json.dump(output, fwrite, indent = 4)