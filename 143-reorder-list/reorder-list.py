# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
there are three steps 
1. split
2.reverse
3.merge

"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow=head,head

#step 1: find the middle of list
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
#step 2: reverse the 2nd list
        second=slow.next        #pointer pointing to first element of 2nd list  eg 4->5 (at 4)
        slow.next=None          #spliting into two 
        node=None               #We use node = None to build the reversed second half of the list.  It starts as empty (None) and then we keep attaching nodes in reverse order to it.



        while second:           #while any element is present in 2nd list
            temp=second.next    #we use temp varaible to store or keep track of next element
            second.next=node    #Reverse the pointer: 4 → None
            node=second         #It moves the head of the reversed list to the current node (second).
            second=temp         #increment the second (.next)
        
        first=head              #pointer for first list
        second=node             #pointer for 2nd

        while second:
            temp1=first.next        # storing or tracking the 2nd element 
            temp2=second.next       #same 
            first.next,second.next=second, temp1     #logic    
            first,second=temp1,temp2                #increment 
            



"""
1-2-3-4-5

after splitting :               1-2-3      4-5
after reversal of 2nd list :    1-2-3      5-4
output :    1-5-2-4-3
"""
        
        