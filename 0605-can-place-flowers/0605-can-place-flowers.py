class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = 0
        l = len(flowerbed)

        for i in range(l):  # loop correctly through full range
            # Special case: First index
            if i == 0:
                if flowerbed[i] == 0 and (l == 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    m += 1

            # Special case: Last index
            elif i == l - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    m += 1

            # General case: middle elements
            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                m += 1

            # Early exit if enough flowers placed
            if m >= n:
                return True

        return m >= n
