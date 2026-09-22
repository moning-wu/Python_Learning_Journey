#案例1
# num = int(input("请输入数字:"))
# if num % 2 == 0:
#     print("该数字为偶数")
# else:
#     print("该数字为奇数")

#案例2
# num = int(input("请输入您的年龄:"))
# if num >= 18:
#     print("成年")
# else:
#     print("未成年")

#案例3
# num = float(input("请输入非0数字:"))
# if num >= 0:
#     print("正数")
# else:
#     print("负数")

#案例4
# point = int(input("请输入您的考试分数:"))
# if point >= 60:
#     print("及格")
# else:
#     print("不及格")

#案例5
# point = int(input("请输入您的分数:"))
# if point >= 85:
#     print(f"您的分数为{point} \n 等级为优秀")
# elif 60 <= point < 85:
#     print(f"您的分数为{point} \n 等级为合格")
# else:
#     print(f"您的分数为{point} \n 等级为不及格")


""""
#案例6
money = float(input("请输入本次您的购物金额:"))
if money >= 500:
    print(f"您本次需要支付的购物金额为{money * 0.8} \n您享受的折扣为8折")
elif 300 <= money < 500:
    print(f"您本次需要支付的购物金额为{money * 0.9} \n您享受的折扣为9折")
elif 100 <= money < 300:
    print(f"您本次需要支付的购物金额为{money * 0.95} \n您享受的折扣为95折")
else:
    print(f"您本次购物金额为{money} \n无折扣")
"""

#案例7
V = float(input("请输入您本次的用电额度:"))
if V <= 2880:
    print(f"您本次的用电额度为{V} \n您本月缴纳的电费为{(V * 0.4883):.2f}")
elif 2880 < V <= 4800:
    print(f"您本次的用电额度为{V} \n您本月缴纳的电费为{(2880 * 0.4883 + (V-2880) * 0.5383):.2f}")
else:
    print(f"您本次的用电额度为{V} \n您本月缴纳的电费为{(2880 * 0.4883+(4800-2880) * 0.4883 + (4800-2880) * 0.5383 + (V-4800)*0.7883):.2f}")