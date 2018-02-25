def merge(list, begin, middle, end):
    n1 = middle - (begin + 1)
    n2 = end - middle
    list1 = []
    list2 = []
    for i in range(0, n1):
        list1.append(list[begin+i-1])
    for j in range(0, n2):
        list2.append(list[middle+j])
    list1.append('final')
    list2.append('final')
    i = 0
    j = 0
    print begin
    print end
    for k in range(begin, end):
        if list1[i] <= list2[j]:
            list[k] = list1[i]
            i = i + 1
        else:
            list[k] = list2[j]
            j = j + 1
    return list

def merge_sort(list, begin, end):
    if(begin < end):
        q = (begin + end)/2
        merge_sort(list, begin, q)
        merge_sort(list, q + 1, end)
        merge(list, begin, q, end)

merge_sort([0, 3, 8, 2, 1, 9], 0, 5)
