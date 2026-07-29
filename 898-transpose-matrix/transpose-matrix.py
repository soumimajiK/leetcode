class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r,c = len(matrix), len(matrix[0])
        res = []
        for j in range(c):
            temp = []
            for i in range(r):
                temp.append(matrix[i][j])
            res.append(temp)
        return res
        