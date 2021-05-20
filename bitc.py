import random
file = open('bitc.csv', 'w')
ff = open('e0e1.txt', 'r')
ff1 = open('e1e2.txt', 'r')
count = int(ff.read())
count1 = int(ff1.read())
ff.close()
ff1.close()
file.write('t,n,d,e0,e1,e2,c0,c1,c2\n')
a, xx, minx = 1, 1, 1
e1, c1, n1 = -1, 1, 1
e0, c0 = -1, 1
e2, c2, n2, minx1 = -1, 1, 1, 1  # 数据的预读取和定义
for i in range(600):

    if c0 != 0:  # 算法0；一跌就卖，一涨就买
        if a < xx:
            e0 += a * c0
            c0 = 0
    else:
        if a > xx:
            c0 = 1 / a
            e0 -= 1

    if c1 != 0:  # 算法1：每上涨1.5倍则卖至购买价，跌至一半全卖，涨回来或又跌到0.75则买回
        if a >= 1.5 * n1:
            e1 += a * (c1 - c1 * n1 / a)
            c1 *= n1 / a
            n1 = minx = a
        elif a <= 0.5 * n1:
            e1 += a * c1
            c1 = 0
            n1 = minx = a
    else:
        if a >= n1 * 2 or (a <= n1 * 0.75 and a > minx):
            e1 -= 1
            c1 = 1 / a
            n1 = minx = a

    if c2 != 0:  # 算法2：每上涨2倍则卖至购买价，跌至一半全卖，涨回来或又跌到0.5则买回
        if a >= 2 * n2:
            e2 += a * (c2 - c2 * n2 / a)
            c2 *= n2 / a
            n2 = minx1 = a
        elif a <= 0.5 * n2:
            e2 += a * c2
            c2 = 0
            n2 = minx1 = a
    else:
        if a >= n2 * 2 or (a <= n2 * 0.5 and a > minx1):
            e2 -= 1
            c2 = 1 / a
            n2 = minx1 = a

    if e1 > e0:
        count += 1
    else:
        count -= 1

    if e1 > e2:
        count1 += 1
    else:
        count1 -= 1
# 生成币价

    x = a * random.randint(80, 125) / 100
    file.write('{},{},{},{},{},{},{},{},{}\n'.format(i, a, x - a, e0, e1, e2, c0, c1, c2))
    xx = a
    a = x
    if a < minx:
        minx = a
e1 += c1 * a
e0 += c0 * a
e2 += c2 * a
file.write('{},{},{},{},{},{},{},{},{}\n'.format(600, a, 0, e0, e1, e2, 0, 0, 0))
if e1 > e0:
    count += 10
else:
    count -= 10
if e1 > e2:
    count1 += 10
else:
    count1 -= 10
file.close()
f = open('e0e1.txt', 'w')
f.write('{}'.format(count))
f1 = open('e1e2.txt', 'w')
f1.write('{}'.format(count1))
