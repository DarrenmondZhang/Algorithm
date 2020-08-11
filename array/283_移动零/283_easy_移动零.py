#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (59.74%)
# Likes:    507
# Dislikes: 0
# Total Accepted:    114.3K
# Total Submissions: 191.3K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        1. set loops to count the numbers of zeros, 将非0元素放在前， 0元素放在后
        2. 开辟一个新的数组，loop， 碰到0，往数组后放置，非0，放在数组前
        3. index
        """
        if not nums:
            return 0
        """ O(N^2)
        for i in range(len(nums)):
            if nums[i] == 0 :
                nums.append(0)
                nums.remove(0)
        """

        """O(N)
        # 第一次遍历，j指针记录非零个数，只要是非0的统统赋值给nums[j]
        j = 0  # j始终记录下一个非0元素要放的位置
        for i in range(len(nums)) :
            if nums[i] != 0 :
                nums[j] = nums[i]
                if (i != j) :
                    nums[i] = 0
                j += 1
        """
        
        """ O(N)
        # 第一次遍历，j指针记录非零个数，只要是非0的统统赋值给nums[j]
        j = 0
        for i in range(len(nums)) :
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)) :
            nums[i] = 0
        """

        """O(N)
        # 交换，j表示数组中第一个0元素的位置。
        j = 0
        for i in range(len(nums)):
            # 当前元素如果不为0，就把其换到左边，等于0的交换到右边
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        """

Solution().moveZeroes([0, 1, 0, 3, 12])
# @lc code=end

