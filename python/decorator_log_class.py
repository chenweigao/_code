from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            logging_string = func.__name__ + " was called"
            print(logging_string)
            with open(self.logfile, 'a') as open_file:
                # 打开一个文件用于追加
                open_file.write(logging_string + '\n')
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        print("log!!!")



@logit()
def myfunc():
    pass

myfunc()