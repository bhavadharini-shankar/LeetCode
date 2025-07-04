class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l=len(nums)
        c=0
        left=0
        right=l-1
        nums.sort()
        
        while left<right:
            if nums[left]+nums[right]==k:
                c+=1
                left+=1
                right-=1
            elif nums[left]+nums[right]<k:
                left+=1
            else:
                right-=1

        return c