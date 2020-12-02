'''
假如如下数据对应数据库里面的目录结构记录
1. 假如添加的顺序是无序的，只根据id来进行索引
{
    "data": [
        {
            "id": 1,
            "parent_id": null
        },
        {
            "id": 2,
            "parent_id": 1
        },
        {
            "id": 3,
            "parent_id": null
        },
        {
            "id": 4,
            "parent_id": 3
        },
        {
            "id": 5,
            "parent_id": 4
        },
        {
            "id": 6,
            "parent_id": 4
        },
        {
            "id": 7,
            "parent_id": 3
        },
        {
            "id": 8,
            "parent_id": 7
        },
        {
            "id": 9,
            "parent_id": 7
        },
        {
            "id": 10,
            "parent_id": 7
        },
        {
            "id": 11,
            "parent_id": 3
        },
        {
            "id": 12,
            "parent_id": 11
        },
        {
            "id": 13,
            "parent_id": 11
        },
        {
            "id": 14,
            "parent_id": 11
        },
        {
            "id": 15,
            "parent_id": 11
        },
        {
            "id": 16,
            "parent_id": 11
        },
        {
            "id": 17,
            "parent_id": 3
        },
        {
            "id": 18,
            "parent_id": 17
        },
        {
            "id": 19,
            "parent_id": 17
        },
        {
            "id": 20,
            "parent_id": 17
        }
    ]
}
'''
import json

dict_data = {
    "data": [
        {
            "id": 1,
            "parent_id": None
        },
        {
            "id": 2,
            "parent_id": 1
        },
        {
            "id": 3,
            "parent_id": None
        },
        {
            "id": 4,
            "parent_id": 3
        },
        {
            "id": 5,
            "parent_id": 4
        },
        {
            "id": 6,
            "parent_id": 4
        },
        {
            "id": 7,
            "parent_id": 3
        },
        {
            "id": 8,
            "parent_id": 7
        },
        {
            "id": 9,
            "parent_id": 7
        },
        {
            "id": 10,
            "parent_id": 7
        },
        {
            "id": 11,
            "parent_id": 3
        },
        {
            "id": 12,
            "parent_id": 11
        },
        {
            "id": 13,
            "parent_id": 11
        },
        {
            "id": 14,
            "parent_id": 11
        },
        {
            "id": 15,
            "parent_id": 11
        },
        {
            "id": 16,
            "parent_id": 11
        },
        {
            "id": 17,
            "parent_id": 3
        },
        {
            "id": 18,
            "parent_id": 17
        },
        {
            "id": 19,
            "parent_id": 17
        },
        {
            "id": 20,
            "parent_id": 17
        }
    ]
}

dir_data = dict_data["data"]
print(dir_data)

# 找出parent_id为空的当作根节点
root = []


def find_child(array, item):
    # 此处的遍历查找相当于mysql的where条件
    flag = False
    item["data"] = []
    for j in array:
        if j["parent_id"] == item["id"]:
            item["data"].append(j)
            flag = True
            find_child(array, j)
    if not flag:
        item.pop("data")
        return


for i in dir_data:
    if i["parent_id"] is None:
        # 同时去寻找子节点
        find_child(dir_data, i)
        root.append(i)

print(json.dumps(root))
