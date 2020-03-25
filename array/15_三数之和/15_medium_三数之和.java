/*
 * @lc app=leetcode.cn id=15 lang=java
 *
 * [15] 三数之和
 *
 * https://leetcode-cn.com/problems/3sum/description/
 *
 * algorithms
 * Medium (26.16%)
 * Likes:    1923
 * Dislikes: 0
 * Total Accepted:    182.9K
 * Total Submissions: 699.3K
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
 * ？请你找出所有满足条件且不重复的三元组。
 * 
 * 注意：答案中不可以包含重复的三元组。
 * 
 * 
 * 
 * 示例：
 * 
 * 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
 * 
 * 满足要求的三元组集合为：
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 * 
 * 
 */

// @lc code=start
// a + b = -c 题目转化
// 1. 暴力求解：三重循环，最外层循环为 -target  O(n^3)
// 2. hash表记录
// 3. 双指针，左右下标 夹逼准则 ※
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for(int i = 0; i < nums.length - 2; i++){
            // nums[k]为非负数，就不能满足a+b+c=0了
            if(nums[i] > 0) break;
            // 跳过计算过的数据，同时防止结果重复
            if(i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int leftPoint = i + 1, rightPoint = nums.length - 1;
            while(leftPoint < rightPoint){
                int sum = nums[i] + nums[leftPoint] + nums[rightPoint];
                if(sum < 0){
                    leftPoint++;
                } else if (sum > 0) {
                    rightPoint--;
                } else {
                    res.add(Arrays.asList(nums[i], nums[leftPoint], nums[rightPoint]));
                    while (leftPoint < rightPoint && nums[leftPoint] == nums[leftPoint+1]) {
                        leftPoint++;
                    }
                    while(leftPoint < rightPoint && nums[rightPoint] == nums[rightPoint-1]) {
                        rightPoint--;
                    }
                    leftPoint++;
                    rightPoint--;
                }
            }
        }
        return res;
    }
}

// @lc code=end

