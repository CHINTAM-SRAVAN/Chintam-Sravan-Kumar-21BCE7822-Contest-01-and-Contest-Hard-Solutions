class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        Final=[]
        for i in strs:
            temp=''.join(sorted(i))
            if temp in d.keys():
                d[temp].append(i)
            else:
                d[temp]=[i]
 
        return d.values()
