# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        new=ListNode(0)
        curr=new
        
        for i in arr:
            curr.next=ListNode(i)
            curr=curr.next
        return new.next

            

        