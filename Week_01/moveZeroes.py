#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution(object):
    def moveZeroes(self, nums):
        j = 0;
        for i in xrange(len(nums)):
            if nums[i]:
                nums[j] = nums[i];
                j += 1;
        for i in xrange(j,len(nums)):
            nums[i] = 0;
        return nums;
