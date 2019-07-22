class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n ==0 or n==2:
            return False
        elif n ==1 or n==3:
            return True
        while n%3==0 :
            n = n//3
            if n ==3:
                return True
        return False