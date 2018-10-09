# 查找一个list中最小和最大值，并返回一个tuple

def findMinAndMax(L):
    if len(L)<=0:
        return(None,None)
    else:
        min=L[0]
        max=L[0]
        for x in L[1:]:
            if x<min:
                min=x
            elif x>max:
                max=x
        return(min,max)
