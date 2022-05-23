import pandas

seznam_zvirat = pandas.read_csv("seznam.csv", ";")
print(seznam_zvirat)
print(seznam_zvirat.info())   #513 řádků, 6 sloupců
print(f"Na řádku 34 je zvíře:{seznam_zvirat.iloc[34,1]}")
