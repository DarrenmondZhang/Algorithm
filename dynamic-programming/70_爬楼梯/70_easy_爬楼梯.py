#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (48.10%)
# Likes:    892
# Dislikes: 0
# Total Accepted:    157.9K
# Total Submissions: 328.2K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 : 1 -> f(1)
        # 2 : 0,2 / 1,1 -> f(1) + f(2)
        # 3 : 1,2 / 2,1 -> f(2) + f(3) 
        if (n<=2): return n
        f1, f2, temp = 1, 2, 0
        for i in range(3, n+1):
            temp = f1 + f2
            f1 = f2
            f2 = temp
        return temp




# @lc code=end

