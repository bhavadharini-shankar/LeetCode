class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even1= [s1[0], s1[2]]
        even2= [s2[0], s2[2]]

        odd1= [s1[1], s1[3]]
        odd2= [s2[1], s2[3]]

        even1.sort()
        even2.sort()
        odd1.sort()
        odd2.sort()

        if even1 == even2 and odd1 == odd2:
            return True
        else:
            return False