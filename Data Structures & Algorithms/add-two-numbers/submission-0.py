# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node = ListNode(0)
        curr = node
        while l1 and l2:
            curr_val = l1.val + l2.val + carry
            carry = curr_val > 9
            curr_val %= 10
            curr.next = ListNode(curr_val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            curr_val = l1.val + carry
            carry = curr_val > 9
            curr_val %= 10
            curr.next = ListNode(curr_val)
            curr = curr.next
            l1 = l1.next
        while l2:
            curr_val = l2.val + carry
            carry = curr_val > 9
            curr_val %= 10
            curr.next = ListNode(curr_val)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(1)
        return node.next

        