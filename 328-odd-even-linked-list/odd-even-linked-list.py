#solution using 2 pointers odd and even
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd,even=head, head.next
        even_ptr=even

        while even and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
        odd.next=even_ptr
        return head













# this solution is using arrays 
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next   #
        
        reordered=arr[::2]+arr[1::2]

        new=ListNode(0)
        curr=new
        for i in reordered:
            curr.next=ListNode(i)
            curr=curr.next
        return new.next
