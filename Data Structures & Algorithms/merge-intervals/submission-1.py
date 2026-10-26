class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]
        for interval in sorted_intervals[1:]:
            if end < interval[0]:
                result.append([start, end])
                start = interval[0]
                end = interval[1]
            elif end >= interval[0] and end > interval[1]:
                continue
            elif end >= interval[0] and end < interval[1]:
                end = interval[1]
        
        result.append([start, end])
        return result
            
            
            
        