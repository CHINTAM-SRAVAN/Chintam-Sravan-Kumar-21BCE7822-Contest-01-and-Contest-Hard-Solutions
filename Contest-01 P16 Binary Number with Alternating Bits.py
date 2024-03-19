class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev=-1
        while(n!=0):
            if n%2==0:
                if prev!=0:
                    prev=0
                else:
                    return False
            else:
                if prev!=1:
                    prev=1
                else:
                    return False
            n=n/2
        return True        
