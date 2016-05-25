"""
Given a linked list, reverse it to a new list
For example:
Given a linked list: 1 -> 2 -> 3 -> 4 -> 5
Return:              5 -> 4 -> 3 -> 2 -> 1
"""

import unittest
import util.list_node as li
# from util.list_node import ListNode


class MyTest(unittest.TestCase):

    def assertListNodeEqual(self, l1, l2):
        while l1 is not None and l2 is not None:
            self.assertEqual(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next
        self.assertIsNone(l1)
        self.assertIsNone(l2)

    def test(self):
        solution = Solution()
        e1 = li.get_list_from_array([6, 5, 4, 3, 2, 1])
        a1 = li.get_list_from_array([1, 2, 3, 4, 5, 6])

        self.assertListNodeEqual(e1, solution.reverse(a1))


class Solution(object):

    def reverse(self, head):
        """
        :type head: ListNode
        :rtype: new head for reversed list
        """
        if head is None or head.next is None:
            return head
        tmp = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return tmp
