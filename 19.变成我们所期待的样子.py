import pymysql

conn = None
cursor = None

try:
    # 1.建立连接
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Wuwenhao@2026',
        database='paper_wedding_dress',
        charset='utf8mb4'
    )
    #2.创建字典游标
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    #3.参数化查询
    search_name = input("请输入您要查询的角色名:")
    sql = "select * from paper_wedding_dress.zhi_jia_yi_characters where name = %s"
    #4.执行
    cursor.execute(sql, (search_name,))
    #5.获取单条结果(目前来说学号才是唯一,但是我建库设置了名字唯一，所一用了fetchone而非fetchall)
    result = cursor.fetchone()
    #6.处理结果
    if result:
        print(f"找到角色:{result['name']}")
        print(f"该角色所有信息为{result}")
    else:
        print("找不到喵🐱")
# 7.异常处理
except Exception as e:
    print(f"发生了错误喵~,错误代码:{e}")
    if conn:
        conn.rollback()
#安全关闭
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("再见了喵~")




