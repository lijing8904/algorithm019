#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        nums_map = {};
        for i,n in enumerate(nums):
            element = target - n;
            if element in nums_map:
                return [nums_map[element], i];
            else:
                nums_map[n] = i;
        return [];
