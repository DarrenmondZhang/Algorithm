#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (77.68%)
# Likes:    677
# Dislikes: 0
# Total Accepted:    112.6K
# Total Submissions: 144.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums):
        # res = []
        # n = len(nums)

        # def helper(i, tmp):
        #     res.append(tmp)
        #     for j in range(i, n):
        #         helper(j + 1, tmp + [nums[j]])
        # helper(0, [])
        # return res


        # res = [[]]

        # for num in nums:
        #     res += [curr + [num] for curr in res]
        # return res

        # result = [[]]

        # for num in nums:
        #     newsets = []
        #     for subset in result:
        #         new_subset = subset + [num]
        #         newsets.append(new_subset)
        #     result.extend(newsets)
        # return result

        res =[[]]
        for num in nums:
            newsets = []
            for subset in res:
                new_subset = subset + [num]
                newsets.append(new_subset)
            res.extend(newsets)
        return res
        

Solution().subsets([1,2,3])
# @lc code=end

