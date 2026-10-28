# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current_node = head.next
        previus = head
        previus.next = None
        while current_node.next:
            next_current_node = current_node.next
            current_node.next = previus
            previus = current_node
            current_node = next_current_node
        current_node.next = previus
        return current_node