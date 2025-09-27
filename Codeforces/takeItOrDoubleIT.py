inputStr = input()

n1, n2 = [int(x) for x in inputStr.split()]

if (n1*2)>n2:
    print("take it")
else:
    print("double it")