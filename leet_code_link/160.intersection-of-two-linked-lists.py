#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (30.86%)
# Total Accepted:    195.3K
# Total Submissions: 632.8K
# Testcase Example:  'No intersection: []\n[]'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
# 
# For example, the following two linked lists: 
# 
# A:          a1 → a2
# ⁠                  ↘
# ⁠                    c1 → c2 → c3
# ⁠                  ↗            
# B:     b1 → b2 → b3
# 
# begin to intersect at node c1.
# 
# Notes:
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns. 
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# 
# 
# Credits:Special thanks to @stellari for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, pre, curr):
        if not curr:
            return pre
        link = curr.next
        curr.next = pre
        return self.reverse(curr, link)

    def getIntersectionNode(self, headA, headB):
        """

        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headA.next or not headB or not headB.next:
            return False
        headA = self.reverse(None, headA)
        headB = self.reverse(None, headB)
        isSameVal = False
        target = None
        while headA and headB:
            if headA.val == headB.val:
                isSameVal = True
            if headA.val != headB.val:
                if isSameVal:
                    target =  headA
                    break
                else:
                    break
            headA = headA.next
            headB = headB.next
        
        headB = self.reverse(None, headB)
        headA = self.reverse(None, headA)
        return target

