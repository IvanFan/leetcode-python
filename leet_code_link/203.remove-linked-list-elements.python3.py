#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (33.65%)
# Total Accepted:    156.7K
# Total Submissions: 465.5K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr = head
        pre = None
        while curr:
            if curr.val == val:
                if not pre:
                    head = curr.next
                    curr = curr.next
                else:
                    pre.next = curr.next
                    curr = curr.next
            else:
                pre = curr
                curr = curr.next
        return head

            

