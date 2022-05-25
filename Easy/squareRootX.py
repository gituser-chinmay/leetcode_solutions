class Solution:
    def mySqrt(self, x: int) -> int:
        #Binary search solution
        l = 0
        r = x
        
        while l<=r:
            mid = (l+r)//2
            
            #If square of mid is the input value, then square root of input is mid
            if mid**2 == x:
                return mid
            
            #If square of mid is greater than x, range has to be reduced to [l,mid-1)
            elif mid**2>x:
                r = mid-1
            else:
                l = mid+1
                
        return r
