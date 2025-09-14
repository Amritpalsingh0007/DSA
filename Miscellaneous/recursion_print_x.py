def printer_recursion(x, num):
    """Head Recursion as logic is before function call"""
    if num == 0:
        return
    print(x)
    recursion_printer(x, num - 1)

def recursion_printer(x, num):
    """Tail Recursion or Backtracking as function call is before logic"""
    if num == 0:
        return
    recursion_printer(x, num - 1)
    print(x)

printer_recursion(2, 2)
recursion_printer(1, 4)