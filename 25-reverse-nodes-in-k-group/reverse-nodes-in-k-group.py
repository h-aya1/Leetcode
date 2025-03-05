# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        return prev

    def getKthNode(self, temp: Optional[ListNode], k: int) -> Optional[ListNode]:
        k -= 1  # Adjust k as we start from the 1st node
        while temp is not None and k > 0:
            k -= 1
            temp = temp.next
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevLast = None

        while temp is not None:
            kThNode = self.getKthNode(temp, k)

            if kThNode is None:
                if prevLast:
                    prevLast.next = temp
                break

            nextNode = kThNode.next
            kThNode.next = None  # Disconnect the K-th node

            self.reverseList(temp)

            if temp == head:
                head = kThNode
            else:
                prevLast.next = kThNode

            prevLast = temp
            temp = nextNode

        return head
