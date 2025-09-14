def postfixToPrefix(postfix):
    stack = []

    for i in postfix:
        if i.isalpha():
            stack.append(i)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"{i} {a} {b}")
    return stack[-1]

print(postfixToPrefix("cabd*+ef^/*"))