import re
f1 = open('/home/g/papers/a.txt')
f2 = open('/home/g/papers/b.txt', 'w+')
for s in f1.readlines():
    # 开头不是数字
    if not s[0].isdigit():
        # 去掉回车
        s = s.strip()
        if not s.endswith('.'):
            # 加上空格
            s = s + ' '
            f2.write(s)
        else:
            # 加上回车换行
            s = s + ' ' + '\r\n'
            f2.write(s)
f1.close()
f2.close()
