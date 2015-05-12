def sum100(current=2, sequence='1'):
    """Recursive method for finding sequences that sum to 100."""
    if current <= 9:
        sum100(current+1, sequence+str(current))
        if sequence[-1] != u'-' and sequence[-1] != u'+':
            sum100(current, sequence+u'+')
            sum100(current, sequence+u'-')
    else:
        if tot(sequence) == 100:
            print sequence
            return sequence


def tot(sequence, total=0):
    """Helper method for finding total of string sequence.

    plus_minus = 1 or -1"""
    total = 0
    temp = ''
    counter = 0
    plus_minus = 1
    while counter < len(sequence):
        try:
            int(sequence[counter])
            temp = temp+sequence[counter]
        except ValueError:
            total = total + (int(temp)*plus_minus)
            temp = ''
            if sequence[counter] == u'-':
                plus_minus = -1
            if sequence[counter] == u'+':
                plus_minus = 1
        counter += 1
    total = total + (int(temp)*plus_minus)
    return total

if __name__ == "__main__":
    sum100()
