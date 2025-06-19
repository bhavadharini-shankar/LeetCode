class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        count=0
        for i in range(l):
            if nums[i]==0:
                count+=1
        while 0 in nums:
            nums.remove(0)
        for i in range(count):
            nums.append(0)
        return nums