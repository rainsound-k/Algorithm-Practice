def bubble_sort(a):
    while True:
        changed = False
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                print(a)
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True
    
        if not changed:
            return
    
d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)
