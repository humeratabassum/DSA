# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# #iterative
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev , curr=None , head
#         while curr:
#             nxt=curr.next
#             curr.next=prev
#             prev=curr
#             curr=nxt
#         return prev


#reccursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newhead=head
        if head.next:
            newhead=self.reverseList(head.next)
            head.next.next=head
        head.next=None
        return newhead





        # prev=None
        # current=head

        # while current:
        #     next_node=current.next
        #     current.next=prev
        #     prev=current
        #     current=next_node
        # return prev
        