class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        '''
        triangle = [1]
        for i in range(1,rowIndex+1):
            triangle = [x+y for x,y in zip([0]+triangle,triangle+[0])]
        return triangle
        '''
        row = [1]
        for i in range(rowIndex):
            row = [1] + [row[j] + row[j+1] for j in range(i)] + [1] # 学会用列表解析
        return row