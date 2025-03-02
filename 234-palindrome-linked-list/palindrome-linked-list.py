# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return True
      
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        left = head
        right =  prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        
        return True
