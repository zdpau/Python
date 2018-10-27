# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
# -*- coding: UTF-8 -*-
def is_palindrome(n):
	return str(n)==str(n)[::-1] # str(n)[::-1]实现字符串翻转
  # return n == int(str(n)[::-1])
   
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
