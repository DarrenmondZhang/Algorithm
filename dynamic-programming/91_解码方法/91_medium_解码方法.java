/*
 * @lc app=leetcode.cn id=91 lang=java
 *
 * [91] 解码方法
 *
 * https://leetcode-cn.com/problems/decode-ways/description/
 *
 * algorithms
 * Medium (23.99%)
 * Likes:    452
 * Dislikes: 0
 * Total Accepted:    58.5K
 * Total Submissions: 243.2K
 * Testcase Example:  '"12"'
 *
 * 一条包含字母 A-Z 的消息通过以下方式进行了编码：
 * 
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * 
 * 
 * 给定一个只包含数字的非空字符串，请计算解码方法的总数。
 * 
 * 示例 1:
 * 
 * 输入: "12"
 * 输出: 2
 * 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
 * 
 * 
 * 示例 2:
 * 
 * 输入: "226"
 * 输出: 3
 * 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
 * 
 * 
 */

// @lc code=start
class Solution {
    public int numDecodings(String s) {
        char[] chars = s.toCharArray();
        return decode(chars, chars.length - 1);
    }

    int decode(char[] chars, int index) {
        if (index <= 0){
            return 1;
        }
        int count = 0;

        char curr = chars[index];
        char prev = chars[index - 1];

        if (curr > '0'){
            count = decode(chars, index - 1);
        }
        if (prev == '1' || (prev == '2' && curr <= '6')){
            count += decode(chars, index - 2);
        }
        return count;
    }
}
// @lc code=end

