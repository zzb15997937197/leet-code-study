"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

str_input = "LEETCODEISHIRING"


def set_empty_string(a, num):
    for k in range(0, num):
        a[k] = ""
    return a


def convert(s, numRows):
    target = list()
    count = 0
    son = []
    for i in range(0, numRows):
        son.append("")
    for i in s:
        if count < numRows:
            son[count] = i
            count = count + 1
        elif count == numRows:
            print("列表:", tuple(son), "中间元素:", i)
            target.append(tuple(son))
            son = set_empty_string(son, numRows)
            # 添加中间元素
            for j in range(numRows, 2, -1):
                print("j", j)
                # 因为空的那个总是从numRows-1的位置开始的，对应列表的下标为numRows-2
                son[j - 2] = i
                target.append(tuple(son))
                son = set_empty_string(son, numRows)
            count = 0

    print("target", target)
    # 遍历结果，逐行遍历
    result = []
    for i in range(0, numRows):
        for j in target:
            if j[i] != "":
                result.append(j[i])
    return result


target = convert(str_input, 3)
target = "".join(target)
print("得到的字符串为:", target)
