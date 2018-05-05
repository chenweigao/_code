# def divide(a, b):
#     try:
#         return True, a/b
#     except ZeroDivisionError:
#         return False, None

# x, y = 1, 0
# success, result = divide(x, y)
# if not success:
#     print('Invaild inputs')
# else:
#     print(result)

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

x, y = 5, 0
try:
    result = divide(x, y)
except ValueError as identifier:
    print('Invalid inputs')
else:
    print(result)