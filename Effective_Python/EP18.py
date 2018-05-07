# log function
import datetime


def log(message, *values, when=None):
    when = datetime.datetime.now() if when is None else when
    if not values:
        print('%s: %s' % (when, message))
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s: %s' % (when, values_str))


log('my numbers are:', 1, 2, 3)
log('have no number')

favorite = [7, 13, 99]
log('Favorite number: ', *favorite)
