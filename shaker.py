def shaker_sort(arr):
    n = len(arr)
    comparisons = 0
    moves = 0
    left = 0
    right = n - 1

    while left < right:
        # left → right
        for i in range(left, right):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                moves += 1
        right -= 1

        # right → left
        for i in range(right, left, -1):
            comparisons += 1
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                moves += 1
        left += 1

    return comparisons, moves