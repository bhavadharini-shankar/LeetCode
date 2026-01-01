class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d="".join(map(str, digits))
        k=int(d)
        add=k+1
        result=list(map(int, str(add)))
        return result