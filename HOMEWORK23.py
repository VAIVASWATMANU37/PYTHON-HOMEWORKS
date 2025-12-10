class ITR:
    def __init__(self):
        self.V = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
    def convert(self, N):
        RN = ""
        for x, y in self.V:
            while N >= x:
                RN += y
                N -= x
        return RN
CVT = ITR()
UI=int(input("ENTER THE NUMBER TO BE CONVERTED!!! "))
print(CVT.convert(UI))
