# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # Collect values in order
        vals = []
        temp = head
        while temp:
            vals.append(temp.val)
            temp = temp.next

        # Reorder values by odd index first, then even
        reordered = vals[::2] + vals[1::2]

        # Create a new linked list
        dummy = ListNode(0)
        curr = dummy
        for val in reordered:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
