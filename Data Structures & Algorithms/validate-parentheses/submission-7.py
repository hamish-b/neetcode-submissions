class Solution:
    def isValid(self, s: str) -> bool:
        
        # add element to stack if the bracket is open, pop if closed and correct type

        stack = []

        for b in s:
            if b in ["(", "{", "["]:
                stack.append(b)
            elif b in [")", "}", "]"] and len(stack) != 0:
                c = stack.pop(-1)
                if (c == "(" and b != ")") or (c == "{" and b != "}") or (c == "[" and b != "]") :
                    return False
            else:
                return False
                    
        return len(stack) == 0
