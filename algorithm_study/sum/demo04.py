# [1,2,3,4,[5,6,[7,8]]]
a = [1, 2, 3, 4, [5, 6, [7, 8]]]


## 解题思路: 遍历列表，如果元素为列表，那么就递归遍历每一项求和，再将返回的和作为上一次递归的值，如果不是列表，那么就将项数添加求和

def func(list_data):
    sum_data = 0
    for i in list_data:
        if not isinstance(i, list):
            sum_data += i
        else:
            sum_data += func(i)
    return sum_data


print(func(a))
