# this is same as postfix to infix but here we will do a + b not b + a where a is pop first and b is poped next from stack

def prefixToInfix(prefix):
    stack = []

    for i in prefix[::-1]:
        if i.isalpha():
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({a} {i} {b})")

    return stack[-1]

print(prefixToInfix("/*c+a*bd^ef"))