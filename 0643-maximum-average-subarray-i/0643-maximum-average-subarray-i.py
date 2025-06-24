class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=len(nums)
        first_sum=sum(nums[:k])
        max_sum=first_sum

        for i in range(k,l):
            first_sum+=nums[i]-nums[i-k]
            max_sum=max(max_sum,first_sum)

        return max_sum/k