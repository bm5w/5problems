def combine(list1, list2):
    output = []
    for i in range(max(len(list1), len(list2))):
        output.append(list1[i])
        output.append(list2[i])
    return output
