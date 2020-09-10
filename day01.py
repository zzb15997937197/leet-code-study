# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates = [1, 2, 4, 3, 6]
target = 5


def find_combination(candidates, target):
    result = []
    for i in candidates:
        p = target - i
        if p in candidates:
            if (p, i) not in result:
                result.append((i, p))
    return result


res = find_combination(candidates, target)
print(res)

# 列表推导式
a = {x for x in candidates if x not in [1, 6]}
print(a)
