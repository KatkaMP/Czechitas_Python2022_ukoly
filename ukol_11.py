import requests

# r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_praha.csv")
# open("zam_praha.csv", "wb").write(r.content)

# r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_plzeň.csv")
# open("zam_plzeň.csv", "wb").write(r.content)

# r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_liberec.csv")
# open("zam_liberec.csv", "wb").write(r.content)

# r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
# open("platy_2021_02.csv", "wb").write(r.content)

import pandas

liberec = pandas.read_csv("zam_liberec.csv", ",")
plzen = pandas.read_csv("zam_plzeň.csv", ",")
praha = pandas.read_csv("zam_praha.csv",",")
mzdy = pandas.read_csv("mzdy.csv",",")

# print(liberec)
# print(plzen)
# print(praha)

liberec["mesto"] = "Liberec"
plzen["mesto"] = "Plzeň"
praha["mesto"] = "Praha"

# print(liberec)
# print(plzen)
# print(praha)

vsichni_zamestnanci = pandas.concat([liberec, plzen, praha], ignore_index=True)
print(vsichni_zamestnanci)
zamestnanci_plat = pandas.merge(vsichni_zamestnanci, mzdy, on=["cislo_zamestnance"])
print(zamestnanci_plat)

pocet_radku1 = vsichni_zamestnanci.shape[0]
pocet_radku2 = zamestnanci_plat.shape[0]
print(pocet_radku1)
print(pocet_radku2)

prumerne_platy = zamestnanci_plat.groupby("mesto").mean()["plat"]
print(prumerne_platy)