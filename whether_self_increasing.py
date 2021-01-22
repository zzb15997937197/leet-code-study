# 判断data是否连续自增
temp = 0
f = open("data", "r")
success = True
while True:
    lines = f.readlines(1000)
    if not lines:
        f.close()
        break
    for line in lines:
        line = int(line.strip())
        if line > temp:
            temp = line
        else:
            success = False
            print("错误，出现递减情况!", "temp=", temp, "line=", line)

if success:
    print("序列全局递增!")
else:
    print("序列出现错误情况!")
