class Solution(object):
    def lengthOfLongestSubstring(self, s):
       maxi=0
       n=len(s)
       for i in range(n):
            substring=""
            for j in range(i,n):
                if s[j] in substring:
                    break
                else:
                    substring+=s[j]

            if len(substring)>maxi:
                maxi=len(substring)  
       return maxi
