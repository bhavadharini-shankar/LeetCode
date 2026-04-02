class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0   # dp[i-2]
        curr = 0   # dp[i-1]
        
        for num in nums:
            temp = curr
            curr = max(curr, prev + num)
            prev = temp
        
        return curr