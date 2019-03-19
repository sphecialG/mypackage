def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''
    out = items.copy()
    for i in range(len(out)):
        for j in range(len(out)-i-1):
            if items[j] > items[j+1] :
                items[j], items[j+1] = items[j+1], items[j]

    # return sorted array
    return items

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1

    return items

def quick_sort(items):
    '''Return array of items, sorted in ascending order'''

    if len(items) <= 1:
        return items
    else:
        return quick_sort([i for i in items[1:] if i <= items[0]]) + [items[0]] + quick_sort([i for i in items[1:] if i > items[0]])
