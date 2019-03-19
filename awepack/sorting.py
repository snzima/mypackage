'''
Implementation of some of the sorting algorithms.
'''
def    bubble_sort(items):
    '''
    Implementation of bubble sort
    '''
    out = items.copy() # in place protection on items
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]     # Swap!

    return out

def    merge_sort(items):
    '''
    Implementation of merge sort
    '''
    def    merge(str1, str2):
        new_list = []
        while len(str1) > 0 and len(str2) > 0:
            if str1[0] < str2[0]:
                new_list.append(str1[0])
                str1.pop(0)
            else:
                new_list.append(str2[0])
                str2.pop(0)

        if len(str1) == 0:
            new_list = new_list + str2
        if len(str2) == 0:
            new_list = new_list + str1

        return new_list

    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2)

def    quick_sort(items, index=-1):
    '''
    Quick sort Implementation
    '''
    len_i = len(items)
    if len_i <= 1:
        return items
    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)
    small = quick_sort(small)
    large = quick_sort(large)
    return small + dup + large
