d = {"zhang":'666',"duo":777}
while True:
    n = input("请输入你的用户名：")
    if n in d:
        break 
    else:
        print('您输入的用户名不存在，请重新输入')
        # continue
        
count = 5
while True: # 也可以while count
    x = input("请输入您的密码：")
    if x == d[n]:
        print('进入系统')
        break 
    else:
        count -=1
        if count > 0: # 用while count就不用这个判定了
            print("您输入的密码不正确，还有 %s 次机会" %count)
        else:
            print("shabi")
            break # 必须要有，要不然会一直重复输入密码
