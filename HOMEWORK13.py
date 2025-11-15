I = input("ENTER YOUR AGE- ")
if I.isdigit():
    A = int(I)
    if 0 < A < 130:
        print(f"NICE TO THAT YOUR AGE IS {A} YEARS")
        if A % 2 == 0:
            print("AND YOUR AGE IS EVEN :-)")
        else:
            print("AND YOUR AGE IS ODD :-)")
    else:
        print("ERROR 404")
else:
    print("ERROR 303")