stack = []
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
for t in tokens:
    if t not in ["+", "-", "*", "/"]:
        stack.append(int(t))
    else:
        left, right = stack.pop(), stack.pop()
        if t == "+":
            stack.append(left + right)
        elif t == "-":
            stack.append(right - left)
        elif t == "*":
            stack.append(left * right)
        else:
            stack.append(int(right / left))
print(stack[-1])