from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        totaldeintervalos = 0
        indice = 0

        for i in range(1, len(intervals)):
            if intervals[indice][1] > intervals[i][0]:
                totaldeintervalos += 1
                indice = indice if intervals[indice][1] < intervals[i][1] else i
            else:
                indice = i

        return totaldeintervalos

#Codigo base de interval scheduling usado:
#def intervalScheduling(intervals: List[List[int]]) -> List[List[int]]:
#    # Ordena os intervalos com base no tempo de término
#    intervals.sort(key=lambda x: x[1])    
#    selected_intervals = []
#    last_end_time = float('-inf')  # Inicializa o tempo de término do último intervalo selecionado   
#    for interval in intervals:
#        start, end = interval
#        if start >= last_end_time:
            # Se o intervalo atual não se sobrepõe ao último selecionado, selecione-o
#            selected_intervals.append(interval)
#            last_end_time = end  # Atualize o tempo de término do último intervalo selecionado   
#    return selected_intervals
