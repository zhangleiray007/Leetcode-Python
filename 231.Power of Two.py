class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        if n==1 or n==2:
            return True
        while  n % 2 ==0:
            n = n // 2
            if n==1 or n==2:
                return True
        return False