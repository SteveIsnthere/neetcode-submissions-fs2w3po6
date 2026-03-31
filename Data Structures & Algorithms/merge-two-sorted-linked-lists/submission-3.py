# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        c = head

        while list1 or list2:
            if not list1:
                c.next = list2
                list2 = list2.next
                c = c.next
                continue
            if not list2:
                c.next = list1
                list1 = list1.next
                c = c.next
                continue


            if list1.val > list2.val:
                c.next = list2
                list2 = list2.next
            else:
                c.next = list1
                list1 = list1.next

            c = c.next

        return head.next
