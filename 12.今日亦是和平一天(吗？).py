# #求圆的面积与周长
# import math
# def circle_area_cen(r):
#     """
#     计算圆的面积和周长
#     :param r: 圆的半径
#     :return: 圆的面积，圆的周长
#     """
#     return round(math.pi * r ** 2,1),round(2 * math.pi * r,1)  #保留小数：round(...,要保留到几位的数字)
#
# area,cen = circle_area_cen(10)      #多个返回值会组成元组，元组的解包：变量1，变量2 = 元组名()
# print(area,cen)



# #1.定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# def score(fen):
#     """
#     根据分数划分等级
#     :param fen: 用户输入的分数
#     :return: 等级
#     """
#     if fen >= 90:
#         return 'A'
#     elif fen >= 75:
#         return 'B'
#     elif fen >= 60:
#         return 'C'
#     elif fen >= 40:
#         return 'D'
#     else:
#         return '你自己退'
# fen = int(input("请输入分数:"))
# print(score(fen))

# #定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
# def is_palindrome(s):
#     """
#     判断是否为回文
#     :param s: 输入的文本
#     :return: bool值
#     """
#     reversed_s = s[::-1]
#     if s == reversed_s:
#         return True
#     else:
#         return False
# s = input("请输入文本:")
# print(is_palindrome(s))

# #3.定义一个函数:完成时间转换功能，将传入的秒转换为小时、分钟、秒。
# def time_change(sec):
#     """
#     时间转换功能
#     :param sec:输入总秒数
#     :return: 小时，分钟，秒钟
#     """
#     hours = sec // 3600    #总秒数被3600整除就是小时数
#     r_sec = sec % 3600     #这里是被3600整除后的余数
#     minutes = r_sec // 60  #这里是余下来的总秒数被60整除后得到分钟数
#     seconds = r_sec % 60   #这里是最后剩下来的秒数，也可以写成 seconds = (sec % 3600) % 60
#     return hours, minutes ,seconds
# sec = int(input("请输入总秒数:"))
# hours, minutes ,seconds= time_change(sec)
# print(f"结果为{hours}时,{minutes}分,{seconds}秒")


#4.定义一个函数:根据传入的三角形三个边的边长，判定三角形的类型(等边、等腰、普通，或者不能构成三角形)
def triangle_juge(a,b,c):
    """
    判断构不构成三角形
    :param a: 第一条边
    :param b: 第二条边
    :param c: 第三条边
    :return: 类型
    """
    if a+b <= c or c+a <= b or b+c <= a:
        return '不构成三角形'
    elif a == b == c:
        return '等边三角形'
    elif a == b or b == c or c == a:
        return '等腰三角形'
    else:
        return '普通三角形'
a = int(input("请输入第一条边:"))
b = int(input("请输入第二条边:"))
c = int(input("请输入第三条边:"))
print(triangle_juge(a,b,c))