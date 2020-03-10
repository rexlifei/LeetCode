'''
https://leetcode-cn.com/problems/linked-list-cycle-ii/

判断链表是否有环，并找到环起点
用快慢指针，首先判断是否有环，然后找起点
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None

        p1, p2 = head, head
        has_cycle = False
        while True:
            if p1.next == None or p2.next == None or p2.next.next == None:
                return None
            
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                # 有环
                has_cycle = True
                break

        if has_cycle:
            q = head
            while q!= p1:
                q = q.next
                p1 = p1.next
            return q
