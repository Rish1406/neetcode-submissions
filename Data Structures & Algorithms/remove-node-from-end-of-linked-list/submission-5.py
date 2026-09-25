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
        
        del_index=(count-n)#0-indexing

        if del_index==0:#head element to be deleted
            head=head.next
            return head

        curr=head
        while del_index:
            prev=curr
            curr=curr.next
            del_index-=1

        #curr now points to node to be deleted and prev is the node before curr 
        prev.next=curr.next#deleting the node
        return head


        