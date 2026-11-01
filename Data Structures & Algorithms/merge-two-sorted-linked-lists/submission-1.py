# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1
        
        cur_list1 = list1
        cur_list2 = list2
        head = None
        cur_node = None

        while cur_list1 and cur_list2:
            if not head:
                if cur_list1.val > cur_list2.val:
                    head = cur_list2
                    cur_node = cur_list2
                    cur_list2 = cur_list2.next
                else:
                    head = cur_list1
                    cur_node = cur_list1
                    cur_list1 = cur_list1.next
                continue
            
            if cur_list1.val > cur_list2.val:
                cur_node.next = cur_list2
                cur_list2 = cur_list2.next
                cur_node = cur_node.next
            else:
                cur_node.next = cur_list1
                cur_list1 = cur_list1.next
                cur_node = cur_node.next

        while cur_list1:
            cur_node.next = cur_list1
            cur_list1 = cur_list1.next
            cur_node = cur_node.next

        while cur_list2:
            cur_node.next = cur_list2
            cur_list2 = cur_list2.next
            cur_node = cur_node.next
        return head



                


        