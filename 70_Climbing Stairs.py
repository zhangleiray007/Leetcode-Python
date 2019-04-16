class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=5**0.5
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return int(1.0/m*((0.5*(1+m))**(n+1)-(0.5*(1-m))**(n+1)))
			
			
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [None for i in range(n+1)]
        dp[0]=0
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i - 1] + dp[i - 2]
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return dp[n]