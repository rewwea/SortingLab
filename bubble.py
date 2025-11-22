def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    moves = 0

    for i in range(n):
        swapped = False
        for j in range(1, n - i):
            comparisons += 1
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                moves += 1
                swapped = True
        if not swapped:
            break

    return comparisons, moves
