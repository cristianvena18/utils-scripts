import random

s = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()_-+[]{};/':,."

passwordlen = 16
password = "".join(random.sample(s, passwordlen))
print(password)