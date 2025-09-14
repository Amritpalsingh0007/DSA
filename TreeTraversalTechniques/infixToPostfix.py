def infixToPostfix(infix):
    stack =[]
    priority = {"+":1,"-":1,"/":2,"*":2,"^":3, "(":0} #Numbers are just randomly assigned it can be any but make sure they match the operand priority compare to other operands
    postfix = ""
    operand = '+-/*^'
    for i in infix:
        if i in operand:
            while len(stack) > 0 and (priority[i] < priority[stack[-1]]):
                postfix += stack.pop()
            stack.append(i)
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        else:
            postfix += i
    
    while stack:
        postfix += stack.pop()
    return postfix

postfix = (infixToPostfix("c*(a+b*d)/e^f"))
print(postfix)
postfix = (infixToPostfix("a^e^f"))
print(postfix)