def combine(list1, list2):
    """Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3]."""
    output = []
    for i in range(max(len(list1), len(list2))):
        output.append(list1[i])
        output.append(list2[i])
    return output
