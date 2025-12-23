def my_range(start, stop=None, step=1):
    
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("step must not be zero")

    if step > 0:
        while start < stop:
            yield start
            start += step
    
    else:
        while start > stop:
            yield start
            start += step

for i in my_range(5):
    print(i)