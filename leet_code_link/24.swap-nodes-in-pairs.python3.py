#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (39.54%)
# Total Accepted:    218.1K
# Total Submissions: 551.4K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Note:
# 
# 
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pre=head
        cur=pre.next
        prel = None
        while pre and cur:
            link = cur.next
            cur.next = pre
            pre.next = link
            if prel:
                prel.next = cur
            elif prel is None:
                head = cur
            prel = pre
            pre = link
            cur = link.next if link else None
        return head


