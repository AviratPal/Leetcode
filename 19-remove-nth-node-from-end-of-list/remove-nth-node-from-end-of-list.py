class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0)
        dummy.next=head
        current=head
        length=0
        while current!=None:
            length+=1
            current=current.next
        current=dummy
        for _ in range(length-n):
            current=current.next
        current.next=current.next.next
        return dummy.next        

  