# Basic Caculator with "(" and ")". Use stack. 
# Whenever we meet parantices. We put the result that we store onto the stack and process it when meeting ")".
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        sign = 1
        idx = 0
        while idx < len(s):
            c = s[idx]
            if c.isdigit():
                sidx = idx
                while idx < len(s) and s[idx].isdigit():
                    idx += 1
                nums = int(s[sidx:idx])
                res += sign*nums
                idx -= 1
            if c == "+":
                sign = 1
            if c == "-":
                sign = -1
            if c == "(":
                stack.append((res, sign))
                res = 0
                sign = 1
            if c == ")":
                originres, originsign = stack.pop()
                res = originres + originsign*res
            idx += 1
        return res
                