import matplotlib.pyplot as plt
import timeit


def func(n):    #original function
  if n == 0 or n == 1:
    return n
  else:
    return func(n-1) + func(n-2)
  
def func_optimized(n, cache = {}):  #optimized function
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        result = n
    else:
        result = func(n-1) + func(n-2)
    cache[n] = result
    return result

n_values  = range(36)
time_original = []
times_optimized = []
for n in n_values:
   t1 = timeit.timeit(lambda: func(n), number=1)
   t2 = timeit.timeit(lambda:func_optimized(n), number=1)
   time_original.append(t1)
   times_optimized.append(t2)

#plotting results
plt.plot(n_values,time_original,label="Original")
plt.plot(n_values,times_optimized,label="Optimized")
plt.xlabel('n value')
plt.ylabel('Time in seconds')
plt.legend()
plt.show()