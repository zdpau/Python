def normalize(n):
    # 基本想到了，但是对ＭＡＰ函数还是不了解，通过ｍａｐ函数其实就会将normalize函数依次作用到序列的每个元素。
    return n[0].upper() + n[1:].lower()
    
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
