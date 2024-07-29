from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        active_intervals = 0
        min_groups = 0
        
        for interval in intervals:
            start, end = interval
            if active_intervals == 0 or start > end:
                min_groups += 1
            else:
                
                active_intervals += 1
        
        return min_groups