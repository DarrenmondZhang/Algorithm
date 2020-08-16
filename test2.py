class Solution:
    def travel_nums(self, list):
        # print(len(list))
        count =0
        for i in range(1, len(list)-1):
            temp_list = []
            temp_list.append([list[i][1], list[i][0]])
            temp3 = temp_list[0][0]
            temp4 = temp_list[0][1] # 所有遍历出来的需要和他对比

            for j in range(i, len(list) - 1):
                temp = list[j][0] 
                temp2 = list[j][1] 
                if temp == temp3 and temp2 == temp4:
                    count += 1
            # print(list[i][0])
            # print(list[i][1])
        print(count)
        return count
            


    

Solution().travel_nums([
    [6],
    ["beijing","nanjing"],
    ["nanjing", "guangzhou"],["guangzhou", "shanghai"],
    ["shanghai", "beijing"],["fuzhou", "beijing"],
    ["beijing", "fuzhou"]]
    )