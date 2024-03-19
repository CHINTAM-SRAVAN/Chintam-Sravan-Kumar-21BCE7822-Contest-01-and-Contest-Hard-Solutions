class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k=k
        self.q=[]
        
    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.q)>=self.k:
            return False
        else:
            self.q.append(value)
            return True
        
    def deQueue(self):
        """
        :rtype: bool
        """
        if len(self.q)==0:
            return False
        else:
            self.q.pop(0)
            return True
        
    def Front(self):
        """
        :rtype: int
        """
        if len(self.q)==0:
            return -1
        return self.q[0]
        

    def Rear(self):
        """
        :rtype: int
        """
        if len(self.q)==0:
            return -1
        return self.q[-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if len(self.q)==0:
            return True
        else:
            return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.q)==self.k:
            return True
        else:
            return False
        

