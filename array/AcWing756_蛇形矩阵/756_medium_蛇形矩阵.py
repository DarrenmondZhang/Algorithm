# 链接：https://www.acwing.com/problem/content/758/
#
# 输入两个整数n和m，输出一个n行m列的矩阵，将数字 1 到 n*m 按照回字蛇形填充至矩阵中。
#
# 具体矩阵形式可参考样例。
#
# 输入格式
# 输入共一行，包含两个整数n和m。
#
# 输出格式
# 输出满足要求的矩阵。
#
# 矩阵占n行，每行包含m个空格隔开的整数。
#
# 数据范围
# 1≤n,m≤100

# 输入样例：
# 3 3

# 输出样例：
# 1 2 3
# 8 9 4
# 7 6 5

n, m = 3, 3
#  定义四个方向
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

res = [[0] * m for _ in range(n)]

# 当前位置
x, y = 0, 0
# 下一个位置
a, b = 0, 0
# 第几个方向
d = 0

for k in range(1, n * m + 1):
    res[x][y] = k
    a, b = x + dx[d], y + dy[d]
    if a < 0 or a >= n or b < 0 or b >= m or res[a][b]:
        # 走到头 or 走过了 -> 换方向
        d = (d + 1) % 4
        a, b = x + dx[d], y + dy[d]  # 沿着正确方向走一步
    x, y = a, b

for i in range(n):
    for j in range(m):
        print(res[i][j], end=" ")
    print()
