class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=len(nums)
        seen = set(nums)
        result=[]

        for j in range(1,l+1):
            if j not in seen:
                result.append(j)
        return result