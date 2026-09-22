#1
"""
#打印一个长为m，宽为n的长方形
# 1.接收m,n
#长度
m = int(input("请输入长方形的长度:"))
#宽度
n = int(input("请输入长方形的宽度:"))
#打印长方形
for j in range(n):
    for i in range(m):
        print("*",end=" ")
    print()
"""

#2
"""
#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} x {j} = {i * j }",end="\t")
    print()
"""

"""
#根据输入的直角边边长，打印等腰直角三角形
i = int(input("请输入直角边的边长:"))
for j in range(1,i+1):         #控制行
    for k in range(1,j+1):     #控制列
        print("*",end=" ")
    print()
"""

#3
"""
#根据数字，打印出对应的数字金字塔
i = int(input("请输入数字:"))
for j in range(1,i+1):          #j这个值是我需要的行数
    for k in range(1,j+1):      #k这个值是从1一直写到j的意思
        print(f"{k}",end=" ")
    print()
"""

#4

"""
#打印国际象棋棋盘
x = int(input("请输入行数:"))
y = int(input("请输入列数:"))
for i in range(1,x+1):                  #这个i是我的横坐标，他的范围你知道的，从1开始到x
    for j in range(1,y+1):              #同理，j是列数
        if (i + j) % 2 == 0:
            print("X",end=" ")
        else:
            print("Y",end=" ")
    print()                         #注意格式
"""

