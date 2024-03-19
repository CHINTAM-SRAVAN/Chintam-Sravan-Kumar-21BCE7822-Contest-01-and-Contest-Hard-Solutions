class Solution(object):
    def countPrimes(self, n):
        l=[1]*n
        for i in range(2,n):
            if l[i]!=0:
                for j in range(i**2,n,i):
                    l[j]=0
        return l[2:].count(1)

        

        
