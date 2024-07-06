import string
import random

seed = '123456789'
seed = list(seed)
password = []
for x in seed:
    y = random.choice([1,2,3])
    if (y == 1) :
        x = random.choice(string.ascii_letters)
        password.append(x)
    if (y == 2):
        x = random.choice(string.digits)
        password.append(x)
    else:
        x = random.choice(string.punctuation)
        password.append(x)

password = ''.join((str(x) for x in password))

print(password)