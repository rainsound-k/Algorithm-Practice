def sel_sort(a):
    for i in range(0, len(a) - 1):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        
    return a

d = [2, 5, 4, 1, 3]
print(sel_sort(d))
