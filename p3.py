def fib(total=100):
    output = []
    for i in xrange(100):
        if i == 0:
            output.append(0)
        elif i == 1:
            output.append(1)
        else:
            new = output[i-1]+output[i-2]
            output.append(new)
    return output
