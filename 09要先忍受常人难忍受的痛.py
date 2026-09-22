"""
student = (
    ("S001","王 林",85,92,78),
    ("S002","李慕婉",92,88,95),
    ("S003","十 三",78,85,82),
    ("S004","曾 牛",88,79,91),
    ("S005","周 轶",95,96,89),
    ("S006","王 卓",76,82,77),
    ("S007","红 蝶",89,91,94),
    ("S008","徐立国",75,69,82),
    ("S009","许 木",86,89,98),
    ("S010","遁 天",66,59,72)
)
print("学号\t\t姓名\t\t语文\t数学\t英语\t总分\t平均分")
for id,name,chinese,math,english in student:
    total = chinese + math + english
    avg = total/3
    print(f"{id}\t{name}\t{chinese}\t{math}\t{english}\t{total}\t{avg:.1f}")
print()
chinese_scores =[s[2] for s in student]
math_scores =[s[3] for s in student]
english_scores =[s[4] for s in student]
avg1 = sum(chinese_scores) / len(chinese_scores)
avg2 = sum(math_scores) / len(math_scores)
avg3 = sum(english_scores) / len(english_scores)
print(f"语文最高分是:{max(chinese_scores)},最低分是:{min(chinese_scores)},平均分是:{avg1:.1f}")
print(f"数学最高分是:{max(math_scores)},最低分是:{min(math_scores)},平均分是:{avg2:.1f}")
print(f"英语最高分是:{max(english_scores)},最低分是:{min(english_scores)},平均分是:{avg3:.1f}")
print()
print("成绩优秀的学生")
for id,name,chinese,math,english in student:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"学号：{id} 姓名:{name} 总分: {total} 平均分:{avg:.1f}")
"""

football_set = {"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
basketball_set = {"张铁","墨居仁","王林","姜老道","李华元","厉飞雨","云露","曾牛","王蝉","韩立","天运子"}
french_set = {"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
art_set = {"遁天","天运子","韩立","虎咆","姜老道","紫灵"}
#同时法语和艺术
fa_set = french_set & art_set
print(fa_set)
#同时四门
all_set = football_set & basketball_set & french_set & art_set & fa_set
print(all_set)
#只修足球不修篮球
fb_set = football_set - basketball_set
print(fb_set)
#每个学生选修的课程数量
all_list = [*football_set,*basketball_set,*fb_set,*art_set]
for name in all_list:
    print(f"{name}选修的课程数量是:{all_list.count(name)}")