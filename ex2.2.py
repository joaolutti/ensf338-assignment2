import json
import timeit
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(20000)
import threading
threading.stack_size(33554432)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open('ex2.json') as f:
    data = json.load(f)

times = []
for i, arr in enumerate(data):
    print(f"Input {i}: {len(arr)} elements")
    t = timeit.timeit(lambda: func1(arr, 0, len(arr)-1), number=10)
    print(f"Average time: {t/10:.6f} seconds\n")
    times.append(t/10)

sizes = [len(arr) for arr in data]
plt.plot(sizes, times, 'bo')
plt.xlabel('Input Size')
plt.ylabel('Time (Seconds)')
plt.title('Running Time for "func1"')
plt.show()
