"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#2 passes to be done. First pass you make a copy of each node with just value and a hash map that has {key(original node):value(copy of the original node)}. Second pass you assign next and random using the created hasMap
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        orgToCopy={None:None}#edge case at line 22 and 23, if cur.next or cur.random is Null
        cur=head
        while cur:#first pass
            copy=Node(cur.val)
            orgToCopy[cur]=copy
            cur=cur.next
        
        cur=head
        while cur:#second pass
            copy=orgToCopy[cur]
            copy.next=orgToCopy[cur.next]
            copy.random=orgToCopy[cur.random]
            cur=cur.next

        return orgToCopy[head]
        