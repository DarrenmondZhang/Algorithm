#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
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
        # 两个指针i 和 j
        j = 0
        for i in range(len(nums)) :
            # 当前元素如果不为0， 就把其换到左边， 等于0的交换到右边
            if nums[i] != 0 :
                nums[j], nums[i] = nums[i],nums[j]
                j += 1



# @lc code=end

