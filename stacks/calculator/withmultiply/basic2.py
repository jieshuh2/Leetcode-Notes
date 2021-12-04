# We deal with * or / first and treat it as one value and put that to the stack
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 0
        idx = 0
        signs = []
        while idx < len(s):
            c = s[idx]
            if c == "*":
                sign = 1
            if c == "/":
                sign = -1
            if c == "+":
                signs.append(1)
            if c == "-":
                signs.append(-1)
            if c.isdigit():
                sidx = idx
                while idx < len(s) and s[idx].isdigit():
                    idx += 1
                num = int(s[sidx:idx])
                idx -= 1
                if sign == 1:
                    prev = stack.pop()
                    num *= prev
                    sign = 0
                elif sign == -1:
                    prev = stack.pop()
                    num = int(prev / num)
                    sign = 0
                stack.append(num)
            idx += 1
        sign = 1
        res = stack[0]
        for i in range(1,len(stack)):
            res += signs[i - 1]*stack[i]
        return res
            