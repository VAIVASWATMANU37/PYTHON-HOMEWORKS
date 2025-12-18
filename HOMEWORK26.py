#Normal Writing Editon(somewhat)
class Fédération_Internationale_de_le_Automobile__World_Endurance_Championship:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    def display_details(self):
        print(f"Car Name: {self.name}, Category: {self.category}")
LE_MANS_GRAND_TOURING_PROTOTYPE=Fédération_Internationale_de_le_Automobile__World_Endurance_Championship("LMGTP", "FOR 24HOURS OF ENDURANCE")
GRANDTOURER_TYPE_3=Fédération_Internationale_de_le_Automobile__World_Endurance_Championship("GT3", "FOR RACING")
print("CARS DETAILS:")
LE_MANS_GRAND_TOURING_PROTOTYPE.display_details()
GRANDTOURER_TYPE_3.display_details()