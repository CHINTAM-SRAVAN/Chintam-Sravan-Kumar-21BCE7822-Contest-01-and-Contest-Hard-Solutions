class Solution(object):
    def singleNumber(self, nums):
        ones=0
        twoes=0
        for i in nums:
            ones=((ones^i)&(~twoes))
            twoes=((twoes^i)&(~ones))
        return ones



        
