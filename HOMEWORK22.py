import random
LC = "abcdefghijklmnopqrstuvwxyz"
UC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = "0123456789"
AC = LC + UC + N
L = 11
PS = ""
for i in range(L):
    PS += random.choice(AC)
print("YOUR RANDOM PASSWORD IS ", PS)