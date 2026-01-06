class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        i=0
        k=1
        while i<len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                k+=1
                i+=1

        return k