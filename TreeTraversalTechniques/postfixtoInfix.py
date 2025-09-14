def postfisToInfix(postfix):
    stack =[]
    operators = '+-/*^'
    for i in postfix:
        if i in operators:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"({a} {i} {b})")
        else:
            stack.append(i)
    return stack.pop()

postfix = (postfisToInfix("cabd*+ef^/*"))
print(postfix)