class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=len(nums)
        count=0
        result=[]

        for i in range(0,l):
            for j in range(0,l):
                if nums[i]>nums[j]:
                    count+=1
            result.append(count)
            count=0

        return result