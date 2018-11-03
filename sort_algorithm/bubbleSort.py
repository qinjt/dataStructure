from swap import swap

def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if(lyst[i] < lyst[i - 1]):
                swap(lyst, i, i-1)
            i += 1
        n -= 1
