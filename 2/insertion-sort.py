def insertion_sort(a):
    for j in range(1,len(a)):
        chave = a[j]
        i = j - 1
        #quando -1 entao preencheu o primeiro valor a[0]
        while i > -1 and a[i] > chave:
            a[i + 1] = a[i]
            i = i - 1
        a[i+1] = chave
        print i
        print a
    return a

insertion_sort([5,6,3,13,1])
