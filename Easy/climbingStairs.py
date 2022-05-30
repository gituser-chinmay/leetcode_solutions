class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        else:
            dp = []
            #First two terms are taken as 1 and 2 since you can either climb one or two steps at a time
            dp.append(1)
            dp.append(2)
            #Addition of (n-1) and (n-2) up till n gives the number of ways n can be reached
            for i in range(2,n+1):
                dp.append(dp[i-1]+dp[i-2]) 
            
            return dp[n-1]
