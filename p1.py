def p1_for(input_list):
    """Compute some of numbers in list with for loop."""
    out = 0
    for i in input_list:
        out += i
    return out


def p1_while(input_list):
    """Compute some of numbers in list with while loop."""
    out = 0
    count = 0
    while count < len(input_list):
        out += input_list[count]
    return out


def p1_rec(input_list, out=0):
    """Compute some of numbers in list with for loop."""
    if len(input_list) > 0:
        p1_rec(input_list[1:], out+input_list[0])
    else:
        return out
