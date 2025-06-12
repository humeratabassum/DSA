# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        curr=head

        while curr and curr.next:
            if curr.val==curr.next.val:
                while curr and curr.next and curr.val==curr.next.val:
                    curr=curr.next
                prev.next=curr.next
                
            else:
                prev=prev.next
            curr=curr.next
        return dummy.next

"""
curr=curr.next
Keeps moving curr forward as long as the same value repeats.
Helps skip all duplicate nodes in a group (like 3 → 3 → 3).


prev.next = curr.next
Cuts out the whole duplicate group.
Links the last unique node (prev) to the next new value after duplicates.


"""

       