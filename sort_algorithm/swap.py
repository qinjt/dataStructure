def swap(lyst, i, j):
    '''
    Exchange the items at positions i and j
    :param lyst: list
    :param i: int
    :param j: int
    :return: none
    '''
    tmp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = tmp