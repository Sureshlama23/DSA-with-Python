import time
def takedtime(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        function(*args, **kwargs)
        after = time.time()
        func_name = function.__name__
        print(f'{func_name} function execution time taked {after - before}')
    return wrapper
@takedtime
def myfunc(x):
    result = 1
    for i in range(1,x):
        result *=i
        
myfunc(100000)