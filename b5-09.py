import time

def time_this(num_runs=1):
    def outer(func):
        def wrapper():
            i = 1
            avg = 0
            while i <= num_runs:
                start = time.time()
                result = func()
                avg += time.time() - start
                i += 1
            print(avg / num_runs)
            return result
        return wrapper
    return outer


@time_this(num_runs=10)
def f():
    for i in range(100000):
        pass


f()