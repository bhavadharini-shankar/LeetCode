class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p=s.split()
        count=len(p[-1])
        return count