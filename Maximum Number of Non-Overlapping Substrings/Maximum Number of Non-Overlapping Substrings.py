from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        caracteres_unicos = set(s)
        intervals = {}
        for i in caracteres_unicos:
            primeiro_indice = s.index(i)   
            ultimo_indice = s.rindex(i) + 1
            intervals[i] = [primeiro_indice, ultimo_indice]

        valid_intervals = []
        #intervalos válidos
        for i in set(s):
            v1 = comeco = intervals[i][0]
            v2 = fim = intervals[i][1]
            while True:
                tudo = set(s[comeco:fim])
                for j in tudo:
                    comeco = min(comeco, intervals[j][0])
                    fim = max(fim, intervals[j][1])
                if (comeco, fim) == (v1, v2):
                    break           
                v1, v2 = comeco, fim
            
            valid_intervals.append([v1, v2])
        # Ordenar os intervalos
        valid_intervals.sort(key=lambda x: x[1])
        result = []
        prev_fim = float('-inf')
        for comeco, fim in valid_intervals:
            if comeco >= prev_fim:
                result.append(s[comeco:fim])
                prev_fim = fim
        return result
