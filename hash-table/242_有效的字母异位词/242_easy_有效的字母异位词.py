#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (59.38%)
# Likes:    214
# Dislikes: 0
# Total Accepted:    114.6K
# Total Submissions: 189.5K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 
# 示例 1:
# 
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s = "rat", t = "car"
# 输出: false
# 
# 说明:
# 你可以假设字符串只包含小写字母。
# 
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. 暴力算法-> sort, sorted_str() 相等？ o(nlogn)
        # return sorted(s) == sorted(t) 

        # 2. hash map -> 统计每个字符的频次
        if (len(s) != len(t)):
            return False
        hash_dict = {}
        for item in s:
            hash_dict[item] = hash_dict.get(item, 0) + 1
        for item in t:
            hash_dict[item] = hash_dict.get(item, 0) - 1

        for i in hash_dict:
            if hash_dict[i] != 0:
                return False
        return True
# @lc code=end

Solution().isAnagram("anagram", "nagaram")