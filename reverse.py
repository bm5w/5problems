"""given string 'hello world', return reverse string 'world hello'"""

def main(inp):
    print inp
    temp = inp.split()
    print temp
    print ' '.join(temp[::-1])

if __name__ == '__main__':
    main('hello world.')