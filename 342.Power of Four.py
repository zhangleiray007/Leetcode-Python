class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num==0 or num==2 or num==3:
            return False
        elif num==1 or num==4:
            return True
        while num % 4 ==0:
            num=num//4
            if num == 4:
                return True
        return False