class Solution:
    def subArrayExists(self,arr,n):

        t = {} # dictionary
        cursum = 0 #prefix sum
        for i in arr:
            cursum += i
            if cursum == 0:
                return True
            if cursum in t:
                return True
            t[cursum] = 1
        return False
