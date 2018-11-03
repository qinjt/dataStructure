from swap import swap

def selectionSort(lyst):
    '''
    complexity analysis: O(n**2)
    :param lyst: sorted list
    :return: none
    '''
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1