import random
file = open('bitc.csv', 'w')
ff = open('count.txt', 'r')
count1 = ff.readlines()
ff.close()
count=[0,0,0,0,0,0]
for i in range(len(count1)):
    count[i]=int(count1[i])
file.write('t,n,e0,e1,e2,e3\n')
# 数据的预读取和定义
a, xx = 1, 1
e0, c0 = -1, 1
e1, c1, n1, minn1 = -1, 1, 1, 1
e2, c2, n2, minn2 = -1, 1, 1, 1
e3, c3, n3, minn3 = -1, 1, 1, 1

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
            n1 = minn1 = a
        elif a <= 0.5 * n1:
            e1 += a * c1
            c1 = 0
            n1 = minn1 = a
    else:
        if a >= n1 * 1.8 or (a <= n1 * 0.75 and a > minn1):
            e1 -= 1
            c1 = 1 / a
            n1 = minn1 = a

    if c2 != 0:  # 算法2：每上涨2倍则卖至购买价，跌至一半全卖，涨回来或又跌到0.5则买回
        if a >= 2 * n2:
            e2 += a * (c2 - c2 * n2 / a)
            c2 *= n2 / a
            n2 = minn2 = a
        elif a <= 0.5 * n2:
            e2 += a * c2
            c2 = 0
            n2 = minn2 = a
    else:
        if a >= n2 * 1.8 or (a <= n2 * 0.5 and a > minn2):
            e2 -= 1
            c2 = 1 / a
            n2 = minn2 = a

    if c3 != 0:  # 算法3：每上涨1.2倍则卖至购买价，跌至0.8全卖，涨回来或又跌到0.8则买回
        if a >= 1.2 * n3:
            e3 += a * (c3 - c3 * n3 / a)
            c3 *= n3 / a
            n3 = minn3 = a
        elif a <= 0.8 * n3:
            e3 += a * c3
            c3 = 0
            n3 = minn3 = a
    else:
        if a >= n3 * 1.2 or (a <= n3 * 0.8 and a > minn2):
            e3 -= 1
            c3 = 1 / a
            n3 = minn3 = a

    if e0 > e1:
        count[0] += 1
    elif e1 > e0:
        count[0] -= 1
    if e0 > e2:
        count[1] += 1
    elif e2 > e0:
        count[1] -= 1
    if e0 > e3:
        count[2] += 1
    elif e3 > e0:
        count[2] -= 1
    if e1 > e2:
        count[3] += 1
    elif e2 > e1:
        count[3] -= 1
    if e1 > e3:
        count[4] += 1
    elif e3 > e1:
        count[4] -= 1
    if e2 > e3:
        count[5] += 1
    elif e3 > e2:
        count[5] -= 1
# 生成币价

    '''x = a * random.randint(80, 125) / 100'''  # 波动大增长多
    x = a * random.randint(910, 1099) / 1000  # 波动小增长少
    file.write('{},{},{},{},{},{}\n'.format(i, a, e0, e1, e2, e3))
    xx = a
    a = x
    if a < minn1:
        minn1 = a
    if a < minn2:
        minn2 = a
    if a < minn3:
        minn3 = a
e0 += c0 * a
e1 += c1 * a
e2 += c2 * a
e3 += c3 * a
file.write('{},{},{},{},{},{}\n'.format(600, a, e0, e1, e2, e3))
if e0 > e1:
    count[0] += 10
elif e1 > e0:
    count[0] -= 10
if e0 > e2:
    count[1] += 10
elif e2 > e0:
    count[1] -= 10
if e0 > e3:
    count[2] += 10
elif e3 > e0:
    count[2] -= 10
if e1 > e2:
    count[3] += 10
elif e2 > e1:
    count[3] -= 10
if e1 > e3:
    count[4] += 10
elif e3 > e1:
    count[4] -= 10
if e2 > e3:
    count[5] += 10
elif e3 > e2:
    count[5] -= 10
file.close()
f = open('count.txt', 'w')
for i in count:
    f.write('{}\n'.format(i))
