#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q: return root;
        left = self.lowestCommonAncestor(root.left, p, q);
        right = self.lowestCommonAncestor(root.right, p, q);
        if not left: return right;
        if not right: return left;
        return root;
