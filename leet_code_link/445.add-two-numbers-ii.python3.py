#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (46.42%)
# Total Accepted:    50.9K
# Total Submissions: 109.7K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        sa = []
        sb = []
        cur1 = l1
        cur2 = l2
        while cur1:
            sa.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            sb.append(cur2.val)
            cur2 = cur2.next
        carry = 0
        start = None
        val = 0
        while sa or sb or carry !=0:
            if not sa and sb:
                val = sb.pop() + carry
            elif not sb and sa:
                val = sa.pop() + carry
            elif sa and sb:
                val = sa.pop() + sb.pop() + carry
            elif not sa and not sb:
                val = carry
            carry, value = divmod(val, 10)
            new_node = ListNode(value)
            new_node.next = start
            start = new_node
            
        return start

        
