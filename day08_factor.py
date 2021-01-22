# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
from distlib.compat import raw_input

print("将每一项获取因子后,作减法，如果减到0，那么该数就为完数!")


def find_number(target):
    res = []
    for i in range(2, int(target) + 1):
        s = i
        for j in range(1, i):
            if i % j == 0:
                s -= j
                if s < 0:
                    continue
        if s == 0:
            print("完数:" + str(i))
            res.append(i)
    # 如果满足条件，添加到res列表里
    return res


if __name__ == "__main__":
    number = raw_input("请输入目标数:")
    data = find_number(number)
    print("所有完数为:" + str(data))
