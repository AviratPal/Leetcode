class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        previous = None
        current = slow
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        left = head
        right = previous
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

        
               

     