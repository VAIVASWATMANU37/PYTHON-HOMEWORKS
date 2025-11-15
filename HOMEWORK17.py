NB = int(input("ENTER A NUMBER- "))
B = ""
N = NB
while N > 0:
    B = str(N % 2) + B
    N = N // 2
print("ITS BINARY EQUIVIVALENT IS", B)