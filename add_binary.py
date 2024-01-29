class Solution:
    def addBinary(self, a: str, b: str) -> str:
        finalBinary = ""
        arrA = [*a]
        arrB = [*b]

        arrA.reverse()
        arrB.reverse()

        print("arrA: ", arrA)
        print("arrB: ", arrB)


        carry = 0
        count = 0
        while True:
            
            if count == len(arrA):
                print(finalBinary)
                return finalBinary
            

            if carry == 0:
                if arrA[count] == "0" and arrB[count] == "0":
                    finalBinary = finalBinary + "0"
                    carry = 0
                if arrA[count] == "0" and arrB[count] == "1":
                    finalBinary = finalBinary + "1"
                    carry = 0
                if arrA[count] == "1" and arrB[count] == "0":
                    finalBinary = finalBinary + "1"
                    carry = 0
                if arrA[count] == "1" and arrB[count] == "1":
                    finalBinary = finalBinary + "0"
                    carry = 1

            if carry == 1:
                if arrA[count] == "0" and arrB[count] == "0":
                    finalBinary = finalBinary + "1"
                    carry = 0
                if arrA[count] == "0" and arrB[count] == "1":
                    finalBinary = finalBinary + "0"
                    carry = 1
                if arrA[count] == "1" and arrB[count] == "0":
                    finalBinary = finalBinary + "0"
                    carry = 1
                if arrA[count] == "1" and arrB[count] == "1":
                    finalBinary = finalBinary + "1"
                    carry = 1
            print(carry)
            count += 1




obj = Solution()

obj.addBinary("0001","0001")