#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (61.15%)
# Likes:    388
# Dislikes: 0
# Total Accepted:    86.5K
# Total Submissions: 138.5K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 
# 
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs):

        # O(N * KlogK)
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            if key not in dict:
                dict[key] = [item]
            else:
                dict[key].append(item)
            # dict[key] = dict.get(key, []) + [item]
        return list(dict.values())  # 快一点
        # return sorted(d.values())

Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# @lc code=end

