import time

def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("Func {}, cost time {}".format(func.__name__, end_time-start_time))
        return res
    return wrapper