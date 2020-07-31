/*
 * @lc app=leetcode.cn id=51 lang=java
 *
 * [51] N皇后
 *
 * https://leetcode-cn.com/problems/n-queens/description/
 *
 * algorithms
 * Hard (70.46%)
 * Likes:    480
 * Dislikes: 0
 * Total Accepted:    52.2K
 * Total Submissions: 74.1K
 * Testcase Example:  '4'
 *
 * n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 * 
 * 
 * 
 * 上图为 8 皇后问题的一种解法。
 * 
 * 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
 * 
 * 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
 * 
 * 示例:
 * 
 * 输入: 4
 * 输出: [
 * ⁠[".Q..",  // 解法 1
 * ⁠ "...Q",
 * ⁠ "Q...",
 * ⁠ "..Q."],
 * 
 * ⁠["..Q.",  // 解法 2
 * ⁠ "Q...",
 * ⁠ "...Q",
 * ⁠ ".Q.."]
 * ]
 * 解释: 4 皇后问题存在两个不同的解法。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 
 * 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自
 * 百度百科 - 皇后 ）
 * 
 * 
 */

// @lc code=start
class Solution {
    int count;

    boolean check(int row, int col, int[] columns) {
        for (int r = 0; r < row; r++) {
            if (columns[r] == col || row - r == Math.abs(columns[r] - col)) {
                return false;
            }
        }
        return true;
    }

    void backtracking(int n, int row, int[] columns) {
        // 是否在所有n行里否摆放好的皇后?
        if (row == n) {
            count++; // 找到新的摆放方式
            return;
        }

        // 尝试着将皇后放置在当前行中的每一列
        for (int col = 0; col < n; col++) {
            columns[row] = col;
            // 检查是否合法，如果合法就继续下一行
            if (check(row, col, columns)) {
                backtracking(n, row + 1, columns);
            }
            // 如果不合法，就不要把皇后放在这列中（回溯）
            columns[row] = -1;
        }
    }

    public List<List<String>> solveNQueens(int n) {
        count = 0;
        backtracking(n, 0, new int[n]);
        return count;
    }
}
// @lc code=end

