class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = Counter()

        for row in matrix:
            matrix_result=tuple(val ^ row[0] for val in row)
            # matrix_result = tuple(row) if row[0] == 0 else tuple(bit ^ 1 for bit in row)
            patterns[matrix_result]+=1
        return max(patterns.values())
            

