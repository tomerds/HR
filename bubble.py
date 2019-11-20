def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if (a[j] > a[j + 1]):
                count += 1
                store = a[j]
                a[j] = a[j + 1]
                a[j + 1] = store

    return (f'Array is sorted in {count} swaps',
            f'First element: {a[0]}',
            f'Last element: {a[-1]}'
            )

print(countSwaps([3,2,1]))