class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        PSE=[]
        PSO=[]
        te=0
        to=0
        for i in range(n):
            if i%2==0:
                te+=nums[i]
                PSE.append(te)
                PSO.append(to)
            else:
                to+=nums[i]
                PSO.append(to)
                PSE.append(te)
        c=0
        for i in range(n):
            if i==0:
                e=PSE[n-1]-PSE[i]
                o=PSO[n-1]-PSO[i]
                if e==o:
                    c+=1
            else:
                e=PSE[i-1]+PSO[n-1]-PSO[i]
                o=PSO[i-1]+PSE[n-1]-PSE[i]
                if e==o:
                    c+=1
        return c
                
            
        
