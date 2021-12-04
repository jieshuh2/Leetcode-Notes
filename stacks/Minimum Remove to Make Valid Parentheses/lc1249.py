# Trick: Turn string into list. If an invalid ")", remove it. The stack store the invalid "(". 
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        string = list(s)
        for idx, c in enumerate(s):
            if c == "(":
                stack.append(idx)
            elif c == ")":
                if len(stack) == 0:
                    string[idx] = ""
                else:
                    stack.pop()
        for idx in stack:
            string[idx] = ""
        return "".join(string)