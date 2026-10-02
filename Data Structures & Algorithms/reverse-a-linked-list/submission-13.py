# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        curr = head

        while curr:
            array.append(curr.val)
            curr = curr.next
        
        curr = head
        for val in reversed(array):
            curr.val = val
            curr = curr.next

        return head
