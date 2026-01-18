class Solution:
    def isValid(self, s: str) -> bool:
        result=[]
        for ch in s:
            if ch == "(":
                result.append(")")
            elif ch == "[":
                result.append("]")
            elif ch == "{":
                result.append("}")
            else:
                if not result:
                    return False
                top = result.pop()
                if top !=ch:
                    return False
        return not result

