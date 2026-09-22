def calc_data(*args,**kwargs):
    """
    计算一组数据里的最大值，最小值和平均值
    :param args: 不定长位置参数，这里用来指代需要计算的这一批数据
    :param kwargs:不定长关键字参数
    round :保留的小数的位数
    print :bool值,来判断是否打印出来
    :return:最小值，最大值，平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)

    if kwargs.get('round') is not None:
        avg_data = round(avg_data,kwargs.get('round'))

    if kwargs.get('print') :
        print(f"最小值是{min_data},最大值是{max_data},平均值是{avg_data}")
    return min_data,max_data,avg_data

print(calc_data())