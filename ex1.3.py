def func(n, cache = {}):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        result = n
    else:
        result = func(n-1) + func(n-2)
    cache[n] = result
    return result
    
def func(n):
  if n == 0 or n == 1:
    return n
  else:
    return func(n-1) + func(n-2)


