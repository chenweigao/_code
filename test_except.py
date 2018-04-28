import sys
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        # return "I am an error!"
        return repr(self.value)
        #repr()函数将对象转化为供解释器读取的形式

def main():
    try:
        print("---- line 1 ----")
        if len(sys.argv) == 2:
            #表示提供了2个参数
            raise MyError('this is my error value 2')
        print("---- line 2 ----")
    except MyError as e:
         print('My exception occurred, value:', e.value)

if __name__ == '__main__':
    main()