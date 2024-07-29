from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        
        initial_energy = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            if current_energy < minimum:
                initial_energy += (minimum - current_energy)
                current_energy = minimum
            
            current_energy -= actual
        
        return initial_energy