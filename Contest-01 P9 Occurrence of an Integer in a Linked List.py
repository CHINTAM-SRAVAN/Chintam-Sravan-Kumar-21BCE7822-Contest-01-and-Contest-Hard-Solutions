class Solution:
    def count(self, head, key):
        c=0
        temp=head
        while(temp is not None):
            if temp.data==key:
                c+=1
            temp=temp.next
        return c
