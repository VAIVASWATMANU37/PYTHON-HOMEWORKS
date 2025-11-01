INPUT=input("ENTER!!!!!!!!!!!!!!!!! ")

if any(char.isalpha() for char in INPUT):
    print("IT CONTAINS A LETTER!!!!")
else:
    print("ERROR 404! NO LETTER FOUND")
