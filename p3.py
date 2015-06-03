"""
Write a function that computes the list of the first 100 Fibonacci numbers. By
definition, the first two numbers in the Fibonacci sequence are 0 and 1, and
each subsequent number is the sum of the previous two. As an example, here are
the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
"""


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
