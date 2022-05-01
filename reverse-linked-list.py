#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        current = head
        previous = None
        forward = current.next
        while current.next:
            current.next = previous
            previous = current
            current = forward
            forward = current.next
            
        current.next = previous
        head = current
        return head