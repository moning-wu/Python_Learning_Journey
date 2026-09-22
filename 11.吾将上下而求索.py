#教务管理系统
student_dict = {}       #样式{昙露凝:{"语文":150,"数学":150,"英语":150},赵暮寻:{...},...}
#菜单制作
menu = """
# # # # # # # # # # # # # # # # # # # # # 【菜  单】# # # # # # # # # # # # # # # # # # # # #
#   1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出系统   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎来到学生管理系统~")
#循环开始
while True:
    print(menu)
    choice = input("请输入您要执行的操作(1-7):")
    match choice:
        #增加学生信息
        case "1":
            name = input("请输入要添加的学生姓名:")
            if name in student_dict:
                print("学生姓名已存在，请重新输入")
                continue
            chinese_score = int(input("请输入语文分数:"))
            math_score = int(input("请输入数学分数:"))
            english_score = int(input("请输入英语分数:"))
            student_dict[name] = {"语文":chinese_score,"数学":math_score,"英语":english_score}   #字典的添加 字典名_dict[key] = {value}
            print("学生信息添加成功~")
        #修改学生信息
        case "2":
            name = input("请输入要修改的学生姓名:")
            if name not in student_dict:
                print("学生姓名不存在，请重新输入")
                continue
            chinese_score = int(input("请输入语文分数:"))
            math_score = int(input("请输入数学分数:"))
            english_score = int(input("请输入英语分数:"))
            student_dict[name] = {"语文": chinese_score, "数学": math_score, "英语": english_score}  ##字典的修改 字典名_dict[key] = {value}
            print("学生修改成功~")
        #删除学生信息
        case "3":
            name = input("请输入要删除的学生姓名")
            if name not in student_dict:
                print("该学生不存在，请重新输入")
                continue
            else:
                del student_dict[name]                    #字典的删除 del 字典名_dict[key]
                print("删除成功OvO")
        #查询学生信息
        case "4":
            name = input("请输入您要查询的学生姓名:")
            if name not in student_dict:
                print("该学生不存在，请重新输入~")
                continue
            else:
                score = student_dict[name]                  #查询字典，指定key 需要查询的东西=字典名称_dict[key]
                print(f"{name}的语文成绩是{score['语文']},数学成绩是{score['数学']},英语成绩是{score['英语']}")
        #列出所有学生信息
        case "5":
            for name in student_dict.keys():               #把字典中所有[key]对应的[value]遍历一遍
                score = student_dict[name]
                print(f"学生姓名:{name},语文:{score['语文']},数学:{score['数学']},英语:{score['英语']}")
        #统计班级成绩
        case "6":
            if len(student_dict) == 0:
                print("当前暂无学生数据！！！请返回~")
                continue
            chinese_list = [score["语文"] for score in student_dict.values()]
            math_list = [score["数学"] for score in student_dict.values()]
            english_list = [score["英语"] for score in student_dict.values()]
            #开始计算最高分，最低分，平均分
            #1.最高分
            chinese_high = max(chinese_list)
            math_high = max(math_list)
            english_high = max(english_list)
            print(f"语文最高分是{chinese_high},数学最高分是{math_high},英语最高分是:{english_high}")
            #2.最低分
            chinese_low = min(chinese_list)
            math_low = min(math_list)
            english_low = min(english_list)
            print(f"语文最低分是{chinese_low},数学最低分是{math_low},英语最低分是:{english_low}")
            #3.平均分
            chinese_avg = sum(chinese_list) / len(chinese_list)
            math_avg = sum(math_list) / len(math_list)
            english_avg = sum(english_list) / len(english_list)
            print(f"语文平均分是{chinese_avg:.1f},数学平均分是{math_avg:.1f},英语平均分是:{english_avg:.1f}")
            #统计姓名
            for name,score in student_dict.items():             #item是字典中由name和score组成的一个小元组
                if score["语文"] == chinese_high:
                    print(f"语文最高分是:{name}")
                if score["数学"] == math_high:
                    print(f"数学最高分是:{name}")
                if score["英语"] == english_high:
                    print(f"英语最高分是:{name}")
        #登出系统
        case "7":
            print("Bye~")
            break
        #防崩溃机制
        case _:
            print("非法操作！！！")