#定义空字典
shopping_cart = {}        #例: shopping_cart = {"Mate80":{"price":6999,"num":2},"鼠标"：{}}
menu = """
#######购物车系统#######
#     1.添加购物车     #
#     2.修改购物车     #
#     3.删除购物车     #
#     4.查询购物车     #
#     5.退出购物车     #
"""
print("欢迎使用购物车系统~")     #不参与循环
while True:                  #循环开始
    print(menu)
    #执行操作
    choice = input("请输入您所执行的操作(1-5):")
    match choice:
        case "1":
            goods_name =input("请输入您的商品名称:")
            if goods_name in shopping_cart:              #保证商品不存在于字典内
                print("商品已存在，请重新选择~")
                continue                                 #满足条件后循环继续
            goods_price =float(input("请输入您的商品名称:"))
            goods_num =int(input("请输入您的商品名称:"))
            shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
            print("商品添加成功~")
        case "2":
            goods_name = input("请输入您的商品名称:")
            if goods_name not in shopping_cart:
                print("商品不存在，请重新输入~")
                continue
            goods_price = float(input("请输入您的商品名称:"))
            goods_num = int(input("请输入您的商品名称:"))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("商品修改成功~")
        case "3":
            goods_name = input("请输入您的商品名称:")
            if goods_name not in shopping_cart:
                print("商品不存在，请重新输入~")
            else:
                del shopping_cart[goods_name]
                print("删除成功OvO")
        case "4":
            for goods_name in shopping_cart.keys():                  #查询字典
                goods_item = shopping_cart[goods_name]               #goods_item 是由查询所有goods_name这个key所得到的value，组成的子字典
                print(f"商品名称:{goods_name},商品价格:{goods_item['price']},商品数量:{goods_item['num']}")
        case "5":
            print("Bye~")
            break                     #while循环结束
        case _ :
            print("警告，非法操作！")


