"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下:
1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
5.退出购物车
"""
class Goods:
    def __init__(self,name,price,num):
        self.name= name
        self.price=price
        self.num=num

    def __str__(self):
        return f"商品名称:{self.name}，商品价格:{self.price}，商品数量:{self.num}"

    # 修改商品信息
    def update(self, price=None, num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num


class ShoppingCart:
    system_version = "1.0"
    system_name = "购物车管理系统"

    def __init__(self):
        self.shopping_cart_list= []  #空列表，存放添加信息
    #添加
    def add_goods(self):
        name = input("请输入您要添加的产品信息:")
        for s in self.shopping_cart_list:
            if s.name == name:
                print("该商品已存在，请重新输入喵❍⩊❍")
                return
        price = round(float(input("请商品输入价格:")),2)
        num = int(input("请商品输入数量:"))
        item = Goods(name,price,num)
        self.shopping_cart_list.append(item)
        print("商品信息添加成功了喵✧₍^˶- ˕ -˵^₎✧")
    #修改
    def update_goods(self):
        name = input("请输入您要修改的产品信息:")
        for s in self.shopping_cart_list:
            if s.name == name:
                print(f"该商品当前信息为{s}")
                price = round(float(input("请输入更新后的价格:")),2)
                num = int(input("请输入更新后的数量:"))
                s.update(price,num)
                print("商品信息修改成功~")
                print(f"当前该商品信息为{s}")
                return
        print("未找到商品信息！！")
    #删除
    def del_goods(self):
        name = input("请输入您要删除的产品信息:")
        # 判断商品是否存在
        for s in self.shopping_cart_list:
            if s.name == name:
                self.shopping_cart_list.remove(s)
                print("删除成功")
                return
        print("未找到该商品")
    #查询
    def list_shopping_cart(self):
        for s in self.shopping_cart_list:
            print(s)
    #计算
    # 计算购物车总金额
    def calc_total(self):
        total = 0
        for s in self.shopping_cart_list:
            total += s.price * s.num
        print(f"当前购物车商品总金额为：{total:.2f} 元")


    #运行
    def run_shopping_cart(self):
        print(f"欢迎使用购物车管理系统 V{ShoppingCart.system_version}")
        menu = """
        #######购物车系统#######
        #     1.添加购物车     #
        #     2.修改购物车     #
        #     3.删除购物车     #
        #     4.查询购物车     #
        #     5.计算购物车     #
        #     6.退出购物车     #
        
        """
        print("欢迎使用购物车系统~")
        while True:
            print(menu)
            choice = input("请输入您要执行的操作1-6:")
            try:
                match choice:
                    case "1":
                        self.add_goods()
                    case "2":
                        self.update_goods()
                    case "3":
                        self.del_goods()
                    case "4":
                        self.list_shopping_cart()
                    case "6":
                        print("再见了喵(｡í ˰ ì｡)~")
                        break
                    case "5":
                        self.calc_total()
                    case _:
                        print("根本就没有这种选项啊喵ㅎㅅㅎ")
            except ValueError as err:
                print(f"输入值不对喵，错误为{err}")
            except Exception as e:
                print(f"要出错了喵,错误为{e}")

#test
if __name__ == '__main__':
    manager = ShoppingCart()
    manager.run_shopping_cart()

