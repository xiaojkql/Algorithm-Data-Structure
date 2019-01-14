import copy



"""
注意 [1,2,3] * num 是深度复制
[[4,5,6]]*num是浅复制，每一行都是指向同一个的

"""


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rowN,colN = len(M),len(M[0])
        ans =[[None for _ in range(colN)] for i in range(rowN)]
        for i_ in range(rowN):
            for j_ in range(colN):
                ans[i_][j_] = copy.copy(smoother(M,i_-1,j_-1,rowN,colN)) # 注意这里的关联关系
            print(ans)
        return ans

def smoother(M,x,y,rowN,colN):
    sums = 0
    count = 0
    for i in range(x,x+3):
        for j in range(y,y+3):
            if (i < 0 or i > rowN-1 or j<0 or j>colN-1):
                continue
            else:
                sums += M[i][j]
                count += 1
    return sums//count

if __name__ == "__main__":
    solution = Solution()
    print(solution.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))