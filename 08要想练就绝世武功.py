# s = [1,2,3,4,5]
# print(s[0:-2:2])
# print(type(s[0:-2:2]))


# #1.定义列表
# num_list = []
# #2.用户输入十个数字
# for i in range(10):
#     num = int(input("请输入一个整数："))
#     num_list.append(num)
# print(num_list)
# #3.排序
# num_list.sort()
# print(num_list)
# #最大最小平均值
# print("最大值是:",max(num_list))
# print("最小值是:",min(num_list))
# print("平均值是:",sum(num_list) / len(num_list))


# #两个列表合并去重
# num_list1 = [1,2,3,4,5,6,7,8,9,10]
# num_list2 = [1,24,3,4,5,6,77,8,9,10,100861]
# #合并两个列表
# num_list = num_list1 + num_list2
# #去重
# new_list = []
# for num in num_list:
#     if num not in new_list:    #注意not in后面的列表，这里你出过错
#         new_list.append(num)
# print(new_list)


#输出一些值的平方组成的列表
# new_list =[i**2 for i in range(1,21)]
# print(new_list)

"""
#习题1,将如下多个列表合并为一个列表，并去重重复元素，排好序(升序)后输出到控制台。
list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
list2 = ['X','Z','T','Y','D','E','F','G']
list3 = ['W','A','S','D']
new_list = list1+list2+list3
fin_list = []
for i in new_list:
    if i not in fin_list:
        fin_list.append(i)
fin_list.sort()              #升序，别记错了
print(fin_list)
"""

"""
#习题2,将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
new_list = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
print(new_list)
"""
"""
#习题3,将如下列表中的正数提取出来，封装为一个新的列表。
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
new_list = [i for i in list1 if i > 0]
print(new_list)
"""

# #判断回文
# #1.输入字符串
# s = input("请输入文本:")
# #判断回文
# if s ==s[::-1]:       #这里注意，出过错，字符串s翻转就是s[::-1],不要画蛇添足
#     print(f"{s}是回文")
# else:
#     print(f"{s}不是回文")

#将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。
#1.用户输入字符串
fin_list = []
for i in range(10):
    s = input(f"请输入第{i+1}个字符串:")
    re_s = s[::-1].upper()
    fin_list.append(re_s)
for item in fin_list:
    print(item)