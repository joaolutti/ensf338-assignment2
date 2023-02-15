def func1(arr, low, high):
    if high - low < 10:  # use insertion sort for small sub-arrays
        for i in range(low+1, high+1):
            j = i
           while j > low and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
    elif low < high:
       pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
