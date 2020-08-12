# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        # 如果两个数相同，那么这两个数的异或操作就等于0
        if len(array) < 2:
            return None

        twoNumXor = None
        for num in array:
            if twoNumXor is None:
                twoNumXor = num
            else:
                twoNumXor = twoNumXor ^ num

        count = 0  # 两个异或结果之后的最后一个1的下标
        while twoNumXor % 2 == 0:
            twoNumXor = twoNumXor >> 1
            count += 1
        mask = 1 << count

        firstNum = None
        secondNum = None
        for num in array:
            if mask & num == 0:
                if firstNum is None:
                    firstNum = num
                else:
                    firstNum = firstNum ^ num
            else:
                if secondNum is None:
                    secondNum = num
                else:
                    secondNum = secondNum ^ num

        return firstNum, secondNum


if __name__ == '__main__':
    s = Solution()
    print(s.FindNumsAppearOnce([1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7]))