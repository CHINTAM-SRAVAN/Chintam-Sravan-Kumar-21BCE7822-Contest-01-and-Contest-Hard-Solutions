#User function Template for python3

class Solution:

    def isPossible(self, S):
        d={}
        for i in S:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        t=0
        for i in d:
            if t!=1 and d[i]%2!=0:
                t+=1
            elif d[i]%2!=0:
               return
        return "Yes"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        if solObj.isPossible(S):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
