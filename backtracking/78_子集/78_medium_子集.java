/*
 * @lc app=leetcode.cn id=78 lang=java
 *
 * [78] 子集
 *
 * https://leetcode-cn.com/problems/subsets/description/
 *
 * algorithms
 * Medium (77.68%)
 * Likes:    677
 * Dislikes: 0
 * Total Accepted:    112.6K
 * Total Submissions: 144.9K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
 * 
 * 说明：解集不能包含重复的子集。
 * 
 * 示例:
 * 
 * 输入: nums = [1,2,3]
 * 输出:
 * [
 * ⁠ [3],
 * [1],
 * [2],
 * [1,2,3],
 * [1,3],
 * [2,3],
 * [1,2],
 * []
 * ]
 * 
 */

// @lc code=start
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        if (nums == null) {return ans;}
        dfs (ans, nums, new ArrayList<Integer>(), 0);
        return ans;
    }

    private void dfs(List<List<Integer>> ans, int[] nums, List<Integer> list, int index){
        // list存储中间结果；ans存储最终结果
        // terminator
        if(index == nums.length){
            ans.add(new ArrayList<Integer>(list));
            return;
        }
        dfs(ans, nums, list, index + 1);  // not pick the number at this index
        list.add(nums[index]);
        dfs(ans, nums, list, index + 1);  // pick the number at this index
    
        // restore state
        list.remove(list.size()-1);
    }
}
// @lc code=end

