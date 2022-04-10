# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:

# První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

# import
from math import ceil

# functions
  # Fce calculates lenght of the phone number
def number_lenght_fce(x): 
  number_len = len(x)
  if number_len ==13:
    print(f"{number_len}")
    if phone_number[0:4] == "+420":                     # if the number lengh is 13, check if the phone number starts with +420
      phone_check = True
    else:
      phone_check = False
  else:
    if number_len == 9:                                 #if the number lenght is not 13, check if the number lenght is 9
      print(f"{number_len}")
      phone_check = True
    else:
      print(f"{number_len}")
      phone_check = False
  return phone_check

  # Fce calculates message price, when each starte 180 symbols cost 3 Kč
def message_price_fce(x):
  return ceil(len(x)/180)*3

phone_number = input("Zadej číslo kam chceš poslat SMS: ")
number_check = number_lenght_fce(phone_number)
print(f"{number_check}")

if number_check == True:
  message = input("Napiš zprávu: ")
  message_price = message_price_fce(message)
  print(f"Message price is: {message_price}")
else:
  print(f"Not correct phone number: {phone_number}!")