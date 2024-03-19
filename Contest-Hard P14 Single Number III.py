class Solution(object):
    def singleNumber(self, nums):
        found=nums[0]
        for i in nums[1:]:
            found^=i
        
        f=found&-found

        a=0
        b=0
        for i in nums:
            if f&i==0:
                a^=i
            else:
                b^=i

        return [a,b]
        
