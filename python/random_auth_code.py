import random
import string

src = string.digits + string.ascii_letters

password = random.sample(src, 4)

print(''.join(password))
