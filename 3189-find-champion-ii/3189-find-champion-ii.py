class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams=[0]*n
        
        for m,n in edges:
            teams[n]=+1

        winner = [i for i in range(len(teams)) if teams[i]==0]
        if len(winner)==1:
            return   winner[0]
        else:
            return -1
