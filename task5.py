# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # Dummy node to start the result list
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get the current values from each list node, or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of values and the carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Append the new value as a node to the result list
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in each input list if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # The real head of the result list is next to the dummy node
