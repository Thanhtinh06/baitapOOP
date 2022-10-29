def merge(array_left, n1, array_right, n2, list_passenger):
    i = j = k = 0
    while i < n1 and j < n2:
        if array_left[i].totalPayment() > array_right[j].totalPayment():
            list_passenger[k] = array_left[i]
            i += 1
        else:
            list_passenger[k] = array_right[j]
            j += 1
        k += 1

    while i < n1:
        list_passenger[k] = array_left[i]
        i += 1
        k += 1
    while j < n2:
        list_passenger[k] = array_right[j]
        j += 1
        k += 1


def mergeSort(list_passenger, n):
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        array_left = list_passenger[:n1]
        array_right = list_passenger[n1:]
        mergeSort(array_left, n1)
        mergeSort(array_right, n2)
        merge(array_left, n1, array_right, n2, list_passenger)

    return list_passenger
