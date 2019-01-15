
# 每一列的元素指向同一个，浅复制
ans = [[1,2,3]]*2
ans[0][0] = 5
print(ans)
# --> print: [[5, 2, 3], [5, 2, 3]]

ans = [[1,2,3] for _ in range(2)]
ans[0][0] = 5
print(ans)
# --> print: [[5, 2, 3], [1, 2, 3]]

isSame = [True,False,True]
print(sum(isSame))