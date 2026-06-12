class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ret = ""
        if num1 == "0" or num2 == "0":
            return "0"

        def multiply(digit, suffix):
            carry = 0
            res = ""
            for n in reversed(num1):
                d = int(n)
                product = d * digit + carry
                carry = product // 10
                rem = product % 10
                res = str(rem) + res
            if carry:
                res = str(carry) + res
            return res + suffix

        def add(nn1, nn2):
            i1 = len(nn1) -1
            i2 = len(nn2) -1

            c = 0
            res = ""
            while i1 >= 0 and i2 >=0:
                d1 = int(nn1[i1])
                d2 = int(nn2[i2])
                s = d1 + d2 + c
                c = s // 10
                r = s % 10
                res = str(r) + res
                i1 -= 1
                i2 -=1
            
            while i1 >= 0:
                d = int(nn1[i1])
                s = d + c
                c = s // 10
                r = s % 10
                res = str(r) + res
                i1 -= 1
            
            while i2 >= 0:
                d = int(nn2[i2])
                s = d + c
                c = s // 10
                r = s % 10
                res = str(r) + res
                i2 -= 1
            
            if c > 0:
                res = "1" + res

            return res

        suffix = ""
        for d in reversed(num2):
            res = multiply(int(d), suffix)
            # print(d, res)
            ret = add(res, ret)
            # print(res, ret)
            suffix = suffix + "0"

        return ret