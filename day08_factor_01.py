# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
from distlib.compat import raw_input


# 获取该数的所有因子
def find_number(target):
    end = int(target) + 1
    res = []
    for i in range(1, end):
        if int(target) % i == 0:
            res.append(i)
    # 如果满足条件，添加到res列表里
    return res


if __name__ == "__main__":
    number = raw_input("请输入目标数:")
    data = find_number(number)
    print("所有因子为:" + str(data))
