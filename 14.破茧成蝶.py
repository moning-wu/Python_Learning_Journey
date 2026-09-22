# def jc(n):
#     if n==1:
#         return 1
#     else:
#         return n * jc(n-1)
# result=jc(100)
# print(result)



# 定义一个函数，用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
# 具体规则如下:
# 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元(且抵扣金额不能超过商品总价，积分只能整百抵扣)

def calc_order_cost(*args: tuple[str,float,int],coupon: int=0,score :int=0,express: float=0.0) -> float:
    """
    根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
    :param args: 不定长参数，用来展示商品信息是个元组，包含商品名，价格，数量
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 最终计算的价格
    """
#1.计算商品总价格
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
#2.减去优惠
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
#3.减去积分
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
#4.加上运费得出最终结账金额
    total_cost += express
    return total_cost

total = calc_order_cost(("笔记本电脑",12999,3),("试制聚变供能单元",1,200164),coupon=3433,score=1911,express=10.9)
print(total)