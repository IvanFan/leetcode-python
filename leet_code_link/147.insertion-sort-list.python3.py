# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insert(self, head, node):
        pre, curr = None, head   
        while curr.val < node.val:
            pre = curr
            curr = curr.next
        if not pre:
            head = node
        else:
            pre.next = node
        node.next = curr
        return head


    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        tail = head
        curr = head.next
        while curr:
            if curr.val < tail.val:
                # print(curr.val,tail.val)
                link = curr.next
                head=self.insert(head, curr)
                tail.next = link
                curr = link
            else:
                tail = tail.next
                curr = curr.next
        return head


        
