def prefixToPostfix(prefix):
    stack = []

    for i in prefix[::-1]:
        if i.isalpha():
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"{a} {b} {i}")
    return stack[-1]

print(prefixToPostfix("*c/+a*bd^ef"))
