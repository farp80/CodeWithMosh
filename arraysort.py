query_array = ["you", "eat", "be", "around with", "I"]


def sortArray(query_array):
    if len(query_array) == 1 or len(query_array) == 0:
        return query_array

    for i in range(len(query_array)):
        sorted = True
        for j in range(len(query_array) - 1):
            temp = query_array[j]
            temp2 = query_array[j + 1]
            if len(temp) > len(temp2):
                query_array[j] = temp2
                query_array[j + 1] = temp
                sorted = False

        if sorted:
            return query_array


print(sortArray(query_array))
