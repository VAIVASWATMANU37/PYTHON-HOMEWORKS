#Normal Writing Editon
N = int(input("Enter a number: "))
E = [x for x in range(1, N+1) if x % 2 == 0]
O = [x for x in range(1, N+1) if x % 2 != 0]
print("Even numbers:",E)
print("Odd numbers:",O)