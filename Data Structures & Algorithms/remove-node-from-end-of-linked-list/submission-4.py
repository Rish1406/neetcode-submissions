# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        
        del_index=(count-n)#

        if del_index==0:
            head=head.next
            return head

        curr=head
        while del_index:
            prev=curr
            curr=curr.next
            del_index-=1
        
        #curr points to the number to be deleted
        
        prev.next=curr.next
        return head


        