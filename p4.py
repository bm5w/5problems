def largest(input_list):
    output = []
    for i in xrange(len(input_list)):
        biggest = return_biggest(input_list)
        output.append(str(biggest))
        input_list.remove(biggest)
    return int(''.join(output))


def return_biggest(input_list):
    temp = []
    for i in input_list:
        if isinstance(i, int):
            first_num = str(i)[0]
            temp.append(first_num)
    return input_list[temp.index(max(temp))]
