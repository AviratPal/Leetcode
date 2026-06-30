
class Solution(object):
    def reverseList(self, head):
        previous=None
        current=head
        while current!=None:
                next_node=current.next
                current.next=previous
                previous=current
                current=next_node
        return previous
       
  
     
    
     
        