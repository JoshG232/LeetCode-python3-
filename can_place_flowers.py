from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if (len(flowerbed) == 1):
            if (n == 0):
                return True
            if (n == 1 and flowerbed[0] == 0):
                return True
            return False
        
        count = 0
        if (flowerbed[0] == 0 and flowerbed[1] == 0):
            count += 1
            flowerbed[0] = 1
        if (flowerbed[-1] == 0 and flowerbed[-2] == 0):
            count += 1 
        for x in range(0,len(flowerbed)-1):
            try:
                if (flowerbed[x] == 0 and flowerbed[x-1] == 0 and flowerbed[x+1] == 0):
                    count += 1
                    flowerbed[x] = 1
            except:
                print("trolled")
            
        print(count)
        if (n <= count):
            print("True")
            return True
        else:
            print("False")
            return False
obj = Solution()

obj.canPlaceFlowers([0,0,0,0],3)