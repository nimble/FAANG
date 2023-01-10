# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultList = ListNode()
        tail = resultList
          
        while(list1 and list2):
            if(list1.val < list2.val):
                tail.next = list1
                l1 = l1.next
            elif(list1.val > list2.val):
                tail.next = list2
                l2 = l2.next
            tail = tail.next
        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
        
        
        return resultList.next
                
