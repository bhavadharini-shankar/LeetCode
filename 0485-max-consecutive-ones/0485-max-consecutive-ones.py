class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=len(nums)
        count=0
        max_count=0
        for i in range(0,l):
            if nums[i] ==1:
                count+=1
            else:
                if max_count<count:
                    max_count=count
                count=0
        if max_count<count:
            max_count=count

        return max_count
                

            
        
            
