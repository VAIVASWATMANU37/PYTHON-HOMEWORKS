TB = float(input("ENTER THE TOTAL BILL- "))
AP = float(input("ENTER THE AMOUNT PAID- "))
DA = TB - AP
if DA > 0:
    print("THE CUSTOMER OWES ₹{DA}")
elif DA == 0:
    print("THE BILL IS FULLY PAID")
else:
    print(f"OVERPAYED! ₹{(DA)} SHOULD BE RETURNED BACK.")