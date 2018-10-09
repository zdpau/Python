# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格

def trim(s):
    if(s[:1] == ' '):
        s = trim(s[1:]) #通过递归可以消除前面有很多空格
    elif(s[-1:] == ' '):
        s = trim(s[0:-1])
    return s

