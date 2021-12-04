# We insert the index of the first ")" and all the "(" into the stack
# Notice we always have and only have one ")" at the beginning of the stack. 
#   If we pop the ")", That means we meet double ")" so we update the start position of ")"
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxlen = 0
        for idx, c in enumerate(s):
            if c == "(":
                stack.append(idx)
            elif c == ")":
                stack.pop()
                if len(stack) == 0:  
                    stack.append(idx)
                else:
                    maxlen = max(idx - stack[-1], maxlen)
        return maxlen