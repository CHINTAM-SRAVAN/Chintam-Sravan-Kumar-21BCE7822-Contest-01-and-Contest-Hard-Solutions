class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals)
        Final=[]
        start=intervals[0][0]
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            if end>=intervals[i][0]:
                if end<intervals[i][1]:
                    end=intervals[i][1]
            else:
                Final.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
        Final.append([start,end])
        return Final
