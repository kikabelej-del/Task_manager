def hlavni_menu():
 print("Správce úkolu - Hlavní menu")
ukoly = ["1. Přidat nový úkol" ,"2. Zobrazit všechny úkoly" ,"3. Odstranit úkol" ,"4. Konec programu"]
hlavni_menu()
print(ukoly[0])
print(ukoly[1])
print(ukoly[2])
print(ukoly[3])
volba = input("Vyberte možnost (1-4): ")
if volba == "1":
    volba = input("Zadejte název úkolu: ")
if volba == "Úkol 1":
    volba = input("Zadejte popis úkolu: ")
if volba == "Popis pro úkol 1":
    volba = input("Úkol ´Úkol 1´ byl přidán.")
if volba == "2":
    volba = input("Seznam úkolu: 1. Úkol 1 - Popis pro úkol 1")
if volba == "3":
    volba = input("Zadejte číslo úkolu, který chcete odstranit: ")
if volba == "1":
    volba = input("Úkol ´Úkol 1´ byl odstraněn.")
elif volba == "4":
    print("Konec programu.")
else:
    print("Neplatná volba. Zkuste to znovu.")