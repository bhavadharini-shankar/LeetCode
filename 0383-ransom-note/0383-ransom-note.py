class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for a in ransomNote:
            if a not in magazine:
                return False
            magazine = magazine.replace(a, "", 1)
        return True