class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sr = 0 
        er = len(matrix)-1
        sc = 0
        ec = len(matrix[0])-1
        ans = []
        while(sr<=er and sc<=ec):
            for i in range(sc,ec+1):
                ans.append(matrix[sr][i])
            sr+=1
            for i in range(sr,er+1):
                ans.append(matrix[i][ec])
            ec-=1
            if sr <= er:

                for i in range(ec,sc-1,-1): # step -1 define karna para kyuki by default +1 leta h 
                    ans.append(matrix[er][i])
                er-=1
            if sc <= ec:

                for i in range(er,sr-1,-1):
                    ans.append(matrix[i][sc])
                sc+=1
        return ans


        
