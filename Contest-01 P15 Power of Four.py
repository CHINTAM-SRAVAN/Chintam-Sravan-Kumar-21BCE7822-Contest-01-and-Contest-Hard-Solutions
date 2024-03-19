class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t=1
        while(t<=n):
            if t==n:
                return True
            t*=4
        return False
        
