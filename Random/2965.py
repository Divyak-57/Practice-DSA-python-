class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        r,m = 0,0
        for i in range(n*n+1):
            cnt = 0
            for j in range(n):
                for k in range(len(grid[j])):
                    if grid[j][k]==i:
                        cnt +=1
            if cnt == 2:
                r = i 
            if cnt == 0:
                m = i
        
        return [r,m]
        
