import numpy as np
class Solution:
    def inverse_num(self, nums):
        if nums >999999999999:
            return 0
        elif nums ==0:
            return 0
        else:
            if nums>0:
                flag= True
            else:
                flag = False
                nums *= -1
        num_list = list(str(nums))
        # print(num_list)
        while num_list[-1] == '0':
            num_list.pop()
        tmp = "".join(num_list[::-1])
        # if flag:
        #     print(tmp)
        # else:
        #     print('' + tmp)
        # print(tmp)
        return tmp

    def ans(self, n):
        ans = []
        count = 0
        for i in range(10, n):
            temp = self.inverse_num(i)
            temp2 = i * 4
            if temp2 == int(temp):
                count += 1
                ans.append((int(i), int(temp)))
        ans = np.array(ans)
        print(count)
        print(ans)
        return count, ans

Solution().ans(10000)