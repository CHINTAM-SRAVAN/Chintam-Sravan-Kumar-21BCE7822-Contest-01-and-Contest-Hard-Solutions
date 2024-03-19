class RecentCounter(object):

    def __init__(self):
        self.queue=[]
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        k=t-3000
        while(len(self.queue)!=0):
            if self.queue[0]<k:
                self.queue.pop(0)
            else:
                break
        return len(self.queue)
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
