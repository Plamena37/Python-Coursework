from customer import Customer
from taxes import Taxes
t = Taxes()
t.add_taxes("Hristo", 50, 60, 20)
t.add_taxes("Plamena", 50, 120, 20)
t.add_taxes("Toshko", 50, 199, 20)

class platform:
    def __init__(self,name,egn,tel):
        self.Ime = name
        self.egn = egn
        self.tel = tel
        self.c = Customer(self.Ime, self.egn, self.tel)

    def Proverka(self):
        if t.by_names[self.Ime]["Tok"] > 0 or t.by_names[self.Ime]["Voda"] > 0 or  t.by_names[self.Ime]["Telefon"] > 0:
           self.show = "Ток: " + str(t.by_names[self.Ime]["Tok"]) + " лв." + "\nВода: " + str(t.by_names[self.Ime]["Voda"]) + " лв." + "\nТелефон: " + str(t.by_names[self.Ime]["Telefon"]) + " лв."
           print("******************************************")
           print("Клиента с име: " + str(self.Ime) + " ,ЕГН: " + str(self.egn) + " и тел.№: " + str(self.tel))
           print("Има за плащане:\n" + str(self.show))
        else:
           print("******************************************")
           print("Клиента с име: " + str(self.Ime) + " ,ЕГН: " + str(self.egn) + " и тел.№: " + str(self.tel))
           print("Няма сметки за плащане!")

    def Plashtane(self, koe):
        self.koe = koe
        if self.koe == "tok":
            t.by_names[self.c.name]["Tok"] = 0
            print("******************************************")
            print("Токът е платен.")
            print("Ток: " + str(t.by_names[self.c.name]["Tok"]) + " лв.")
            print("Вода: " + str(t.by_names[self.c.name]["Voda"]) + " лв.")
            print("Телефон: " + str(t.by_names[self.c.name]["Telefon"]) + " лв.")
        elif self.koe == "voda":
            t.by_names[self.c.name]["Voda"] = 0
            print("******************************************")
            print("Водата е платена.")
            print("Вода: " + str(t.by_names[self.c.name]["Voda"]) + " лв.")
            print("Ток: " + str(t.by_names[self.c.name]["Tok"]) + " лв.")
            print("Телефон: " + str(t.by_names[self.c.name]["Telefon"]) + " лв.")
        elif self.koe == "tel":
            t.by_names[self.c.name]["Telefon"] = 0
            print("******************************************")
            print("Телефонът е платен.")
            print("Телефон: " + str(t.by_names[self.c.name]["Telefon"]) + " лв.")
            print("Ток: " + str(t.by_names[self.c.name]["Tok"]) + " лв.")
            print("Вода: " + str(t.by_names[self.c.name]["Voda"]) + " лв.")
        elif self.koe == "Всичко":
            t.by_names[self.c.name]["Tok"] = 0
            t.by_names[self.c.name]["Voda"] = 0
            t.by_names[self.c.name]["Telefon"] = 0
            print("******************************************")
            print("Всички сметки са платени.")
            print("Телефон: " + str(t.by_names[self.c.name]["Telefon"]) + " лв.")
            print("Ток: " + str(t.by_names[self.c.name]["Tok"]) + " лв.")
            print("Вода: " + str(t.by_names[self.c.name]["Voda"]) + " лв.")
        else:
            print("********************\"" + self.koe + "\"********************")
            print("Няма такава сметка!")







