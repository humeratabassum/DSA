

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