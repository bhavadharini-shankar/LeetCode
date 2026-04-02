# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # 1. Find peak index
        left=0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        
        # 2. Search in left (ascending)
        res = self.binarySearch(mountainArr, target, 0, peak, True)
        if res != -1:
            return res
        
        # 3. Search in right (descending)
        return self.binarySearch(mountainArr, target, peak + 1, n - 1, False)
    
    
    def binarySearch(self, arr, target, left, right, asc):
        while left <= right:
            mid = (left + right) // 2
            val = arr.get(mid)
            
            if val == target:
                return mid
            
            if asc:
                if val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if val > target:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1