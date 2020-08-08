#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (66.68%)
# Likes:    560
# Dislikes: 0
# Total Accepted:    98.6K
# Total Submissions: 147.7K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
# 
# 
# 
# 例如，给定三角形：
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 
# 
# 说明：
# 
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
# 
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
            dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        """
        # mini, M = triangle[-1], len(triangle)
        # for i in range(M-2, -1, -1):
        #     for j in range(len(triangle[i])):
        #         mini[j] = triangle[i][j] + min(mini[j], mini[j+1])

        # return mini[0]

        dp = triangle  # 将triangle中的值初始化到dp数组中
        # 从倒数第二行开始遍历
        for i in range(len(triangle)-2, -1, -1): 
            # 从左边结点到右边结点
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        print(triangle[0][0])
        return dp[0][0]


# brute-force,递归，n层，left or right: 2^n
# DP 
# 1. 重复性（分治） problem(i, j) = min(sub(i+1, j), sub(i+1, j+1)) + a[i, j]
# 2. 定义状态数组：f[i,j]
# 3. DP方程：f[i,j] = min(f[i+1, j], f[i+1, j+1]) + a[i,j]
# @lc code=end

