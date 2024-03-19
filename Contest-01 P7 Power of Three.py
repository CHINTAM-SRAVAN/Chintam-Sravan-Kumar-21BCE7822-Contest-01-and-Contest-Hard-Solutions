class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t=1
        while(t<=n):
            if t==n:
                return True
            t*=3
        return False
