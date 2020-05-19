import random

s = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passwordlen = 16
password = ""

for i in range(2):
    password = password.join(random.sample(s, passwordlen))

print(password)
