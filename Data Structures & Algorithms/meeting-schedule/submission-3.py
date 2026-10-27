"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        start = sorted_intervals[0].start
        end = sorted_intervals[0].end
        for interval in sorted_intervals[1:]:
            if interval.start < end:
                return False
            start = interval.start
            end = interval.end
        
        return True

