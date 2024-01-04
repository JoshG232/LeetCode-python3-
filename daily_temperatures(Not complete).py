from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        arrDays = []
        days = 0
        compares = 0
        for x in range(len(temperatures)):
            days = 0
            for  i in range(x+1,len(temperatures)):
                compares += 1
                print("Comparing: ", temperatures[x], temperatures[i])
                if temperatures[x] > temperatures[i]:
                    days += 1
                    continue
                else:
                    if (temperatures[i] == temperatures[-1]):
                        arrDays.append(0)
                        break
                    days += 1
                    arrDays.append(days)
                    break
            
            print("Days: ",days)


        
        print(arrDays)
        return arrDays


obj = Solution()

obj.dailyTemperatures([55,38,53,81,61,93,97,32,43,78])