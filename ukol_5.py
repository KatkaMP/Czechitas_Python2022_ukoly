class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr
  
  def get_info(self):
    return f"{self.nazev}; {self.zanr}"

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    self.nazev = nazev
    self.zanr = zanr
    self.delka = delka

  def get_info(self):
    return f"{self.nazev}; {self.zanr}; {self.delka} min"

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
    self.nazev = nazev
    self.zanr = zanr
    self.pocet_epizod = pocet_epizod
    self.delka_epizody = delka_epizody

  def get_info(self):
    return f"{self.nazev}; {self.zanr}; {self.pocet_epizod} epizod; delka epizody{self.delka_epizody} min"

Film1 = Film("Film1", "horor", 120)
print(Film1.get_info())

Polozka1 = Polozka("Serial", "komedie")
print(Polozka1.get_info())

Serial1 = Serial("Serial1", "drama", 10, 45)
print(Serial1.get_info())