def integer(String):
    n=0
    j=0
    for i in range(len(String)-1,-1,-1):
        if String[i]=="1":
            n+=2**j
        j+=1
    return n

def gray(Forward):
    Backward=Forward[::-1]
    Final=[]
    for i in Forward:
        Final.append("0"+i)
    for i in Backward:
        Final.append("1"+i)
    return Final

class Solution(object):
    def grayCode(self, n):
        if n==0:
            return [0]
        if n==1:
            return [0,1]

        Initial=["0","1"]
        t=1
        while t!=n:
            Initial=gray(Initial)
            t+=1

        Final=[integer(i) for i in Initial]
        return Final


        
