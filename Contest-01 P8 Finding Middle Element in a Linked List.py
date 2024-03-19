class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        n=0
        temp=head
        while(temp is not None):
            n+=1
            temp=temp.next
        n=n//2
        temp=head
        for i in range(n):
            temp=temp.next
            
        return temp.data

