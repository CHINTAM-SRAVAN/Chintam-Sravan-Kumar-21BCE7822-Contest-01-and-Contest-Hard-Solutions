class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)

        ml=[]
        maxi=0
        for i in range(n):
            ml.append(maxi)
            if height[i]>maxi:
                maxi=height[i]
        mr=[]
        maxi=0
        for i in range(n-1,-1,-1):
            mr.append(maxi)
            if height[i]>maxi:
                maxi=height[i]
        mr=mr[::-1]
        total=0
        for i in range(n):
            t=min(ml[i],mr[i])-height[i]
            if t>0:
                total+=t
        return total

        
