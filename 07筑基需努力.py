"""
turns = 1

while turns <= 5:
    uesrname = input("请输入您的用户名:")
    password = input("请输入您的密码:")
    if uesrname == "" or password == "":
        print("输入的用户名或密码不能为空，请重新输入！")
        continue
    if uesrname == "刘日天" and password == "040212":
        print("登陆成功，欢迎来到'xiao'子小分队")
        breakpoint()
    elif uesrname == "石见天" and password == "040719":
        print("登陆成功，欢迎来到'xiao'子小分队")
        break
    elif uesrname == "穗穗平安" and password == "040728":
        print("登陆成功，欢迎来到'xiao'子小分队")
        break
    else:
        print("你谁？")

    turns += 1
else:
    print("错误五次，禁止操作")
"""

"""
import random
random_num = random.randint(1, 100)
while True:
    num = int(input("请输入您所猜的的数字:"))
    if random_num > num:
        print("小了兄弟")
    elif random_num < num:
        print("大了兄弟")
    else:
        print("对了兄弟")
        break
print(f"该数字就是{random_num}")
"""

"""
sum = 0
for i in range(1,1001):
    if i % 5 == 0 :
        sum += i
print(sum)
"""

text = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
count1 = 0
count2 = 0
for i in text:
    if i == "a":
        count1 += 1
    elif i == "k":
        count2 += 1
print(f"a的数量为是: {count1}, k的数量是: {count2}")
 