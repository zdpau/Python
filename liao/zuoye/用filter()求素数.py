# 先构造一个从3开始的奇数序列，注意这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 定义一个筛选函数       
def _not_divisible(n):
    return lambda x: x % n > 0 # 这里很重要，我的理解就是第一个n=3?然后所有自然数x%3>0成立的都保留（意思就是3的倍数全删了),然后依次往下
                               # 可是2的倍数怎么弄？


# 最后定义一个生成器，不断返回下一个素数。
# 先返回第一个素数2，然后利用filter()不断产生筛选后的新的序列。
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 由于primes（）是一个无限序列，所以调用时需要设置一个退出循环的条件。         
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
