from typing import List
import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))  
            events.append((end + 1, -1))  
        events.sort()
        
        max_groups = 0
        current_groups = 0
        
        for _, event in events:
            current_groups += event
            max_groups = max(max_groups, current_groups)
        
        return max_groups