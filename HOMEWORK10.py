S = int(input("ENTER THE START OF THE RANGE- "))
E = int(input("ENTER THE END OF THE RANGE- "))
SQ = [i**2 for i in range(S, E + 1)]
OS = [N for N in SQ if N % 2 != 0]
ES = [N for N in SQ if N % 2 == 0]
print(f"\nSQUARE NUMBERS BETWEEN {S} & {E}: {SQ}")
print(f"ODD SQUARE NUMBERS- {OS}")
print(f"EVEN SQUARE NUMBERS- {ES}")