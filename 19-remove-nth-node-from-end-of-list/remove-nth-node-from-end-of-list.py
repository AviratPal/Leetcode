class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0)
        dummy.next=head
        current=head
        slow=dummy
        fast=dummy
        for _ in range(n+1):
            fast=fast.next
        while fast!=None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next        
        
  