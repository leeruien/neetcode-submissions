# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None
        if list1 == None: return list2
        elif list2 == None: return list1
        while list1 or list2:
            if list1 == None: 
                prev.next = list2
                return head
            elif list2 == None: 
                prev.next = list1
                return head
            if list1.val > list2.val:
                new_node = list2
                list2 = list2.next
            else: 
                new_node = list1
                list1 = list1.next
            if head == None: 
                head = new_node
                prev = new_node
            else:
                prev.next = new_node
                prev = prev.next
            print(head)
        return head

        
        