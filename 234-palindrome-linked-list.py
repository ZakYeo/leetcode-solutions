# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # Edge cases: empty list or single-node list
        if not head or not head.next:
            return True

        # Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev, current = None, slow
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_

        # Compare the two halves
        left, right = head, prev
        while right:  # Compare until the end of the reversed half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
