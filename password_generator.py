import itertools

# Funkce pro generování kombinací z jednoho slova
def kombinuj_slovo(slovo, klicova_slova=None):
    kombinace = set()

    # Malá a velká písmena
    kombinace.add(slovo.lower())
    kombinace.add(slovo.upper())
    kombinace.add(slovo.capitalize())

    # Vyměnit malá a velká písmena
    if len(slovo) > 1:
        kombinace.add(slovo.swapcase())

    # Přidat číselné kombinace
    for i in range(0, 100):
        kombinace.add(f"{slovo}{i}")
        kombinace.add(f"{i}{slovo}")

    # Přidat speciální znaky
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
    for char in special_chars:
        kombinace.add(f"{slovo}{char}")
        kombinace.add(f"{char}{slovo}")

    # Kombinace s klíčovými slovy
    if klicova_slova:
        for kl_slovo in klicova_slova:
            kombinace.add(f"{slovo}{kl_slovo}")
            kombinace.add(f"{kl_slovo}{slovo}")

    return kombinace

# Získání vstupních údajů
def ziskej_udaje():
    print("Vyplňte následující údaje:")

    osobni_udaje = {
        "Jméno": input("Jméno: "),
        "Příjmení": input("Příjmení: "),
        "Věk": input("Věk: "),
        "Datum narození": input("Datum narození (DDMMYYYY): "),
        "Telefonní číslo": input("Telefonní číslo: "),
        "Přezdívka": input("Přezdívka: ")
    }

    partnerka_udaje = {
        "Jméno partnerky": input("Jméno partnerky: "),
        "Příjmení partnerky": input("Příjmení partnerky: "),
        "Věk partnerky": input("Věk partnerky: "),
        "Datum narození partnerky": input("Datum narození partnerky (DDMMYYYY): "),
        "Telefonní číslo partnerky": input("Telefonní číslo partnerky: "),
        "Přezdívka partnerky": input("Přezdívka partnerky: ")
    }

    mazlicek_firma = {
        "Jméno mazlíčka": input("Jméno mazlíčka: "),
        "Jméno firmy": input("Jméno firmy: ")
    }

    dite_udaje = {
        "Jméno dítěte": input("Jméno dítěte: "),
        "Přezdívka dítěte": input("Přezdívka dítěte: ")
    }

    lokalita = {
        "Město": input("Město: "),
        "Země": input("Země: "),
        "Oblíbená barva": input("Oblíbená barva: ")
    }

    print("\nZadejte klíčová slova. Pro ukončení zadejte 2x Enter.")
    klicova_slova = []
    while True:
        slovo = input("Zadejte klíčové slovo: ")
        if slovo == "":
            potvrzeni = input("Opravdu ukončit? (Enter pro ano): ")
            if potvrzeni == "":
                break
        else:
            klicova_slova.append(slovo)

    return {
        "osobni_udaje": osobni_udaje,
        "partnerka_udaje": partnerka_udaje,
        "mazlicek_firma": mazlicek_firma,
        "dite_udaje": dite_udaje,
        "lokalita": lokalita,
        "klicova_slova": klicova_slova
    }

# Generování kombinací hesel
def generuj_hesla(udaje):
    vsechny_kombinace = set()

    # Kombinace klíčových slov
    klicova_slova = udaje.get("klicova_slova", [])

    # Projít všechny údaje a generovat kombinace
    for kategorie, data in udaje.items():
        if isinstance(data, dict):
            for klic, hodnota in data.items():
                vsechny_kombinace.update(kombinuj_slovo(hodnota, klicova_slova))
        elif isinstance(data, list):
            for slovo in data:
                vsechny_kombinace.update(kombinuj_slovo(slovo, klicova_slova))

    return vsechny_kombinace

# Uložit hesla do souboru
def uloz_hesla_do_souboru(hesla, soubor="Wordlist.txt"):
    with open(soubor, "w") as f:
        for heslo in hesla:
            f.write(heslo + "\n")
    print(f"Hesla byla uložena do souboru {soubor}.")

# Hlavní funkce
def main():
    udaje = ziskej_udaje()
    hesla = generuj_hesla(udaje)
    uloz_hesla_do_souboru(hesla)

if __name__ == "__main__":
    main()
