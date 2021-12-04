def calculator(inputs):
    res = 0
    sign = 1
    stack = []
    idx = 0
    while idx < len(inputs):
        c = inputs[idx]
        if c.isdigit():
            i = idx
            while i < len(inputs) and inputs[i].isdigit():
                i += 1
            number = int(inputs[idx:i])
            idx = i
            res += number * sign
        elif c == "+":
            sign = 1
            idx += 1
        elif c == "-":
            sign = -1
            idx += 1
        elif c == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
            idx += 1
        elif c == ")":
            res = res * stack.pop() + stack.pop()
            idx += 1
    return res
print(calculator("2+((8+2)+(3-999))"))
print(2+((8+2)+(3-999)))