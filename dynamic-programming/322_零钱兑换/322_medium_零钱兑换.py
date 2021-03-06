#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (40.59%)
# Likes:    737
# Dislikes: 0
# Total Accepted:    115.4K
# Total Submissions: 283.4K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 
# 
# 示例 1:
# 
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 
# 示例 2:
# 
# 输入: coins = [2], amount = 3
# 输出: -1
# 
# 
# 
# 说明:
# 你可以认为每种硬币的数量是无限的。
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={0:0}
        def helper(n):   
            if(n in memo):
                return memo[n]
            res=float("inf")
            for coin in coins:
                if(n>=coin):
                    res=min(res,helper(n-coin)+1)
            memo[n]=res
            return res
        return helper(amount) if(helper(amount)!=float("inf")) else -1

# @lc code=end
# 1. 啥递归
# 2. BFS
# 3. DP
#   a. 分治（子问题） 
#   b. DP array: f(n) = min{f(n - k), (for k in [1, 2, 5])} + 1
#   c. DP 方程