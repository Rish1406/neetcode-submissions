# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next

        #finding the middle element
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #reversing the second half of the linked list
        #note:slow.next is the start of the second half of the linked list
        prev=None
        curr=slow.next
        slow.next=None#breaking the single linked list to 2 linked lists
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            
        #finding the resultant linked list
        first,second=head,prev
        while second:#because second's length is smaller
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            second=tmp2
            first=tmp1
