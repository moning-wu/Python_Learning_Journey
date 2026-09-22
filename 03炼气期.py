a = 100
b = 200
c = 300

d = a
e = b
f = c
a = e
b = f
c = d

print(c,a,b)


drink = '无糖气泡水'
print(f'我老公爱喝{drink}')

total = 10000
password = input("请输入密码:")
print(f"密码正确，{password}")
num = input("本次您的取款金额为：")
print(f"您的余额还剩余：{total - int(num)}")




# num1 = input("请输入第一位数字:")num2 = input("请输入第二位数字:")
print(f"两数之和为:{float(num1) + float(num2)}")






# 案例1，计算输入的三个整数的平均数
num1 = int(input("请输入第一位数字："))
num2 = int(input("请输入第二位数字："))
num3 = int(input("请输入第三位数字："))
print(f"{num1+num2+num3}/3")


# 案例2，计算梯形面积
a = float(input("请输入上底:"))
b = float(input("请输入下底:"))
h = float(input("请输入高:"))
print(f"梯形的面积是：{((a+b)*h)/2}")

#计算圆的周长和面积
import math
r = float(input("请输入圆的半径："))
area = math.pi*r*r
perimeter = 2*math.pi*r
print(f"圆的周长是{perimeter:.2f}，圆的面积是{area:.2f}")

# 计算bmi值
h = float(input("请输入您的身高（cm）为:  "))
g = float(input("请输入您的体重（kg）为:  "))
print(f"您的BMI值为{g / h**2:.2f}")