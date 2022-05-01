class Solution(object):
    def hasCycle(self, head):
        current = head
        while current != None:
            if current.val == None:
                return True
            current.val = None
            current = current.next
        return False