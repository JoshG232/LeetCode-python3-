class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        count = 0
        finalWord = ""

        largest = max(len(word1),len(word2))

        for x in range(largest):
            try :
                finalWord = finalWord + word1[count]   
            except:
                print("oops")
                
            try:
                finalWord = finalWord + word2[count]
            except:
                print("oops2")
            print(finalWord)
            count += 1
        return finalWord
        

obj = Solution()

obj.mergeAlternately("abcasdasdasd","pqrd")