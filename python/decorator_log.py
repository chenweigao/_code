from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called!")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
    return x + x

result = addition_func(4)
print(result)

def logit2(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator


@logit2()
def myfunc1():
    pass

myfunc1()

@logit2(logfile='func2.log')
def myfunc2():
    pass
myfunc2()
