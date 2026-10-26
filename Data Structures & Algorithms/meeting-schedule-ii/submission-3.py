"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        conflict_count = 0
        max_conflict_count = 0

        if not intervals:
            return conflict_count
        
        intervals_with_param = []
        for interval in intervals:
            intervals_with_param.extend([(interval.start, 1), (interval.end,-1)])
        
        sorted_intervals_with_param = sorted(intervals_with_param)

        for interval in sorted_intervals_with_param:
            if interval[1] == 1:
                conflict_count += 1
            else:
                conflict_count -= 1
            max_conflict_count = max(max_conflict_count, conflict_count)

        return max_conflict_count

        