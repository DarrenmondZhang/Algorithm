#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (62.23%)
# Likes:    1223
# Dislikes: 0
# Total Accepted:    162.4K
# Total Submissions: 261K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 
# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 
# 
# 
# 
# 
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 
# 
# 
# 示例：
# 
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """求取最大面积区域
        Args:
            height: a list with height
        Returns:
            The maxArea
        """
        # 双指针解法
        max_area = 0
        leftPointer, rightPointer = 0, len(height) - 1
        while leftPointer < rightPointer:
            if height[leftPointer] < height[rightPointer]:
                area = height[leftPointer] * (rightPointer - leftPointer)
                leftPointer += 1
                max_area = max(area, max_area)
            else:
                area = height[rightPointer] * (rightPointer - leftPointer)
                rightPointer -= 1
                max_area = max(area, max_area)
        return max_area
        
       

# @lc code=end

