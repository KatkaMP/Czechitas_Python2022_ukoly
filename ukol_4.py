class Auto:
  def __init__(self, znacka: str, typ: str, pocet_km: int):
    self.znacka = znacka
    self.typ = typ
    self.pocet_km = pocet_km
    self.status = True

  def pujc_auto(self):
    if self.status == True:
      self.status = False
      return f"Potvrzuji zapůjčení vozidla {self.typ} {self.znacka}."
    else:
      return f"Vozidlo {self.typ} {self.znacka} není k dispozici."

  def get_info(self):
    return f"{self.znacka}; {self.typ}"

Peugeot = Auto ("4A2 3020", "Peugeot 403 Cabrio", 47534)
Skoda = Auto ("1P3 4747", "Škoda Octavia", 41253)

pozadovane_auto = input(f"Zadejte znacku auta, kterou si chcete půjčit: ")

if pozadovane_auto == "Peugeot":
  print(Peugeot.get_info())
  print(Peugeot.pujc_auto())
elif pozadovane_auto == "Škoda":
  print(Skoda.get_info())
  print(Skoda.pujc_auto())
else:
  print("Požadované auto nemáme. K dispozici jsou auta: Peugeot a Škoda")

