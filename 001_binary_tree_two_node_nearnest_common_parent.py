"""
Given a binary tree, return nearest common parent for given two node
For example:
Given binary tree, find the common parent for 5, 6, got 3
    1
  /   \
 2     3
  \   / \
   4 5   6
"""

import unittest
import util.tree_node as tr
# from util.tree_node import TreeNode


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        root = tr.get_tree_from_array([1, 2, 3, '3', 4, 5, 6])
        r1 = root.right
        a1 = r1.left
        b1 = r1.right
        print "a1 is %s, b1 is %s" % (a1.val, b1.val)
        self.assertEqual(r1, solution.findNearestCommon(root, a1, b1))

        r2 = root
        a2 = r2.left.right
        b2 = r2.right.left
        print "a2 is %s, b2 is %s" % (a2.val, b2.val)
        self.assertEqual(r2, solution.findNearestCommon(root, a2, b2))


class Solution(object):

    def findNearestCommon(self, root, n1, n2):
        """
        :type root: TreeNode
        :type n1: TreeNode
        :type n2: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root == n1 or root == n2:
            return root

        ll = self.findNearestCommon(root.left, n1, n2)
        rr = self.findNearestCommon(root.right, n1, n2)

        if ll and rr:
            return root

        if ll:
            return ll
        else:
            return rr
