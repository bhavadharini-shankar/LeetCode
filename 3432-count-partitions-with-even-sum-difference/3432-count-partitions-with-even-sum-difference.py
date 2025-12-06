class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        l=len(nums)
        
        for i in range(1,l):
            a=nums[:i]
            b=nums[i:]

            a1=sum(a)
            b1=sum(b)

            c=a1-b1

            if c%2==0:
                count+=1

        return count
