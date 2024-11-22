class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = Counter()

        for row in matrix:
            # balik=(val ^ row[0] for val in row)
            # print(f'{tuple(val ^ row[0] for val in row)} - {row}')
            matrix_result=tuple(val ^ row[0] for val in row)
            patterns[matrix_result]+=1
            # print(patterns)
        return max(patterns.values())
            

