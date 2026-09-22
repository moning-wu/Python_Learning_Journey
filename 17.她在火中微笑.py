"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功随如下。
1.添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
  1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
  1.2检查学生姓名是否已存在，如果学生不存在，再添加(存在则，不添加)
  1.3 验证成绩范围(0-150分)
  1.4 创建学生对象并添加到系统
2.修改学生成绩:根据输入的学生姓名，修改对应的学生成绩
  2.1 输入要修改的学生姓名
  2.2根据姓名查找该学生，显示该生当前成绩信息
  2.3 输入新的语文、数学、英语成绩
  2.4 更新学生成绩数据
3.删除学生成绩:根据输入的学生姓名，删除对应的学生成绩
4.查询指定学生成绩:根据输入的学生姓名，查找对应的学生成绩，并输出
  4.1输出格式为:“姓名:张三|语文:85|数学:90|英语:88|总分:263
5.展示全部学生成绩:展示出系统中所有学生的成绩
"""

#学生类
class Student:
    def __init__(self, name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名:{self.name}|语文:{self.chinese}|数学:{self.math}|英语:{self.english}"

    #修改学生成绩
    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

#教务系统类类
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.students_list = []   #列表，用于存储录入的学生信息
    #添加学生信息
    def add_student(self):
        name = input("请输入学生姓名:")
        #判断学生是否存在
        for s in self.students_list:
            if s.name == name:
                print("学生已存在，添加失败")
                return
        chinese = int(input("请输入语文成绩:"))
        math = int(input("请输入数学成绩:"))
        english = int(input("请输入英语成绩:"))
        #判断分数是否在0到150之间
        if 0 <= chinese <= 150 and 0 <= math <= 150 and 0 <= english <= 150:
            stu = Student(name,chinese,math,english)
            self.students_list.append(stu)
            print("学生信息添加成功~")
        else:
            print("添加失败，成绩必须在0到150之间！")
        #修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名:")
        #判断学生是否存在
        for s in self.students_list:
            if s.name == name:
                print(f"该生当前成绩是{s}")

                chinese = int(input("请输入语文成绩:"))
                math = int(input("请输入数学成绩:"))
                english = int(input("请输入英语成绩:"))
                # 判断分数是否在0到150之间
                if 0 <= chinese <= 150 and 0 <= math <= 150 and 0 <= english <= 150:
                    s.update_score(chinese,math,english)
                    print("学生信息修改成功~")
                    print(f"当前成绩为{s}")
                    return
                else:
                    print("添加失败，成绩必须在0到150之间！")
                    return
        print("未找到学生,查询失败！！！")
    #删除学生成绩
    def del_student(self):
        name = input("请输入要删除的学生姓名:")
        #判断学生是否存在
        for s in self.students_list:
            if s.name == name:
                self.students_list.remove(s)
                print("删除成功")
                return
        print("未找到该学生")
    #查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名:")
        # 判断学生是否存在
        for s in self.students_list:
            if s.name == name:
                print(f"学生信息:{s}")
                return
        print("未找到该学生!")
    #展示全部学生成绩
    def list_student(self):
        for s in self.students_list:
            print(s)

    #运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("# 1.添加学生 #2.修改学生 3. 删除学生 4.查询指定学生 5.查询所有学生 6.退出系统 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")

            choice = input("\n请输入要执行的操作1-6:")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.del_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("Ciallo~ OvO✌️")
                        break
                    case _:
                        print("这，这不对吧，请输入1-6")
            except Exception:
                print("系统出错了喵，请重新输入喵")
#test
if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()
