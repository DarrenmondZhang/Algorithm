# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):

        if sequence == []:
            return False

        rootNum = sequence[-1]
        del sequence[-1]

        index = None
        for i in range(len(sequence)):
            if index is None and sequence[i] > rootNum:
                index = i
                break
            if index is not None and sequence[i] < rootNum:
                return False

        leftRet = self.VerifySquenceOfBST(sequence[:index])
        rightRet = self.VerifySquenceOfBST(sequence[index:])
        return leftRet and rightRet


