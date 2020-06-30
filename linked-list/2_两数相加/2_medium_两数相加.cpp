/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 *
 * https://leetcode-cn.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (37.11%)
 * Likes:    4523
 * Dislikes: 0
 * Total Accepted:    461.1K
 * Total Submissions: 1.2M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
 * 
 * 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
 * 
 * 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
 * 
 * 示例：
 * 
 * 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
 * 输出：7 -> 0 -> 8
 * 原因：342 + 465 = 807
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        auto dummy = new ListNode(-1);  // 添加虚拟头结点，简化边界情况
        auto cur = dummy;
        int t = 0;  // 表示进位
        // 直到每个链表循环结束且没有进位，循环结束
        while(l1 || l2 || t){
            if(l1) t += l1->val, l1 = l1->next;
            if(l2) t += l2->val, l2 = l2->next;
            cur->next = new ListNode(t % 10);  // t取余的各位是链表中下一个结点的值
            cur = cur->next;  // 插入一个新节点之后，然后将尾结点的指针指向新节点所在位置。
            t /= 10;  // 进位
        }
        return dummy->next;
    }
};
// @lc code=end

