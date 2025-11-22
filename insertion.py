def insertion_sort(arr):
    comparisons = 0
    moves = 0

    for i in range(1, len(arr)):
        key = arr[i]
        moves += 1  # взяли элемент

        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                moves += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
        moves += 1

    return comparisons, moves