"""
Program pre Projekt: Task manager
Umožňuje pridávať, zobrazovať a odstraňovať úlohy uložené v zozname.
"""
# Zoznam pre ukladanie úloh
ukoly = []

def hlavni_menu():
    """Zobrazí hlavné menu programu."""
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu.")

def zobrazit_ukoly():
    """
    Vypíše všetky úlohy v zozname a ich indexom.
    Využitie enumerate pre automaticé číslovanie od 1.
    """
    # Vrátíme False, aby mazanie vedelo, že nie je čo mazať.
    
    print("\nSeznam úkolů: ")
    for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
    return True

def pridat_ukol():
    """
    Požiada užívateľa o názov a popis úkolu.
    Spraví validáciu, aby vstupy neboli prázde.
    """
    nazev = input("Zadejte název úkolu: ").strip()
    popis = input("Zadejte popis úkolu: ").strip()

    if not nazev or not popis:
        print("Neplaná volba. Opakujte volbu.")
        return

    novy_ukol = {"nazev": nazev, "popis": popis}
    ukoly.append(novy_ukol)
    print(f"Úkol '{nazev}' byl úspěšně přidán.")

def odstranit_ukol():
    """
    Zobraí úlohu a umožní užívateľovi jednu úlohu vymazať podľa císla.
    Obsahuje validáciu rozsahu a typu vstupu.
    """
    if not zobrazit_ukoly():
        return

    try:
        index = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if 1 <= index <= len(ukoly):
            odstraneny = ukoly.pop(index - 1)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        else:
            print("Neplaná volba.")
    except ValueError:
        print("Neplaná volba. Opakujte volbu.")

# --- Hlavná smyčka ---
def main():
    """Hlavné funkcie pre spustenie celého programu."""
    while True:
        hlavni_menu()
        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu (zadejte 1-4).")

if __name__ == "__main__":
    main()