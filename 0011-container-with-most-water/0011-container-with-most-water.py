class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=len(height)
        area=0
        hl=0
        hr=l-1

        while hl<hr:
            h=min(height[hl],height[hr])
            w=hr-hl
            a=h*w
            if a>area:
                area=a
            if height[hl]>height[hr]:
                hr-=1
            else:
                hl+=1
        return area