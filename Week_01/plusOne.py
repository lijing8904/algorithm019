#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution(object):
    def plusOne(self, digits):
        digits_plus = 0;
        for i,n in enumerate(digits):
            digits_plus += n*10**(len(digits)-(i+1));
        digits_str = str(digits_plus + 1);
        lst = [int(i) for i in digits_str];
        if (len(lst) < len(digits)):
            for i in xrange(len(digits)-len(lst)):
                lst.insert(i,0);
        return lst;

