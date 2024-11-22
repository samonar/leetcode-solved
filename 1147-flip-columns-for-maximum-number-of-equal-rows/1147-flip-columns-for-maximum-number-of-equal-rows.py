class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = Counter()

        for row in matrix:
            matrix_result=tuple(val ^ row[0] for val in row)
            patterns[matrix_result]+=1
        return max(patterns.values())
            

