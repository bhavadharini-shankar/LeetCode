class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = len(nums)
        max_c = 0
        index = 0  

        for i in range(l):
            if nums[i] == 0:
                k -= 1

            if k < 0:
                if nums[index] == 0:
                    k += 1
                index += 1 

            c = i - index + 1
            if c > max_c:
                max_c = c

        return max_c
