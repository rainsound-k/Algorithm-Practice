def ins_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

d = [2, 5, 4, 1, 3]
print(ins_sort(d))
