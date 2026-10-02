# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        array = []

        while curr:
            array.append(curr.val)
            curr = curr.next
        
        array = list(reversed(array))
        index = 0

        curr = head
        while curr:
            curr.val = array[index]
            index += 1
            curr = curr.next
        
        return head
        



