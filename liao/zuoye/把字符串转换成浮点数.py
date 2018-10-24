# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce

def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    s1, s2 = s.split('.')
    def fn1(x, y):
        return x*10 + y
    def fn2(x1, y1):
        return x1*0.1 + y1
    def char2num(s):
        return DIGITS[s]
    return reduce(fn1, map(char2num, s1)) + reduce(fn2, map(char2num, s2[::-1])) * 0.1
