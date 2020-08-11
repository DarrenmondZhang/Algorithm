#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (26.16%)
# Likes:    1923
# Dislikes: 0
# Total Accepted:    182.9K
# Total Submissions: 699.3K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)
        if (not nums or length<3):
            return []

        for i in range(length):
            if nums[i] > 0:
                break
            
            # 需要和上一次枚举的数不相同，去掉重复情况
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            leftPoint, rightPoint = i + 1, length - 1
            while leftPoint < rightPoint:
                total = nums[i] + nums[leftPoint] + nums[rightPoint]
                if total < 0:
                    leftPoint += 1
                elif total > 0:
                    rightPoint -= 1
                else:
                    res.append([nums[i], nums[leftPoint], nums[rightPoint]])
                    while leftPoint < rightPoint and nums[leftPoint] == nums[leftPoint+1]: leftPoint += 1  # 去重
                    while leftPoint < rightPoint and nums[rightPoint] == nums[rightPoint-1]: rightPoint -= 1  # 去重
                    leftPoint += 1
                    rightPoint -= 1
                    
        return res  

# @lc code=end