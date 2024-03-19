def secondhigh(nums,i):
    nums[i]=-1
    return nums.index(max(nums))

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        count={}
        n=len(s)
        for i in s:
            if i not in count.keys():
                count[i]=1
            else:
                count[i]+=1


        final=""

        keys=count.keys()
        values=count.values()
        n=len(keys)
        if n==1:
            if count[keys[0]]==1:
                return keys[0]
            return ""

        i=values.index(max(values))
        first=keys[i]
        values[i]-=1
        i=secondhigh(values[:],i)
        second=keys[i]
        values[i]-=1
        while True:
            final+=first
            final+=second
            
            count[first]-=1
            count[second]-=1

            i=values.index(max(values))
            first=keys[i]
            values[i]-=1

            i=secondhigh(values[:],i)
            second=keys[i]
            values[i]-=1

            if count[first]==0:
                return final

            if count[second]==0:
                if count[first]==1:
                    return final+first
                else:
                    return ""

            
