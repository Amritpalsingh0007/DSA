# Step 1: Reverse the infix (Note to replace ')' with '(' and vice versa after reversing) 
# Step 2: convert it to Postfix
# Step 3: Reverse the postfix equation
# BOOM we have a prefix expression from infix

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

def reverseInfix(infix):
    infix = [ i for i in infix]
    i = 0 
    j = len(infix) - 1
    while i < j:
        infix[i], infix[j] = infix[j], infix[i]
        if infix[i] == ")":
            infix[i] = "("
        if infix[j] == "(":
            infix[j] = ")"
        i += 1
        j -= 1
    return "".join(infix)

infix = "c*(a+b*d)/e^f"
reversed_infix = reverseInfix(infix)
print(reversed_infix)
postfix = (infixToPostfix(reversed_infix))
print(reverseInfix(postfix))