"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        head = ListNode(0)
        p3 = head
        carry = 0
        while(p1 != None or p2 != None):
            if(p1 != None):
                carry += p1.val
                p1 = p1.next
            if(p2 != None):
                carry += p2.val
                p2 = p2.next
            p3.next = ListNode(carry%10)
            p3 = p3.next
            carry /= 10
        if carry == 1:
            p3.next = ListNode(carry)
        return head.next