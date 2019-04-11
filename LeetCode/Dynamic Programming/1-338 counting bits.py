class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]*(num+1)
        for i in range(num+1):
            ans[i] = ans[i>>1] + (1 if i&1 else 0) # 位与的运算规则
        return ans
