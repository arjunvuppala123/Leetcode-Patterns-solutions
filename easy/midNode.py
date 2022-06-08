# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp1 = head
        while temp1:
            length += 1
            temp1 = temp1.next
        mid = int(length/2)
        ctr = 0
        while head:
            if ctr == mid:
                return head
            ctr += 1
            head = head.next
        return head