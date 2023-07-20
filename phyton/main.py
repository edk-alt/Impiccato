#a = input('inserisci un numero: ');
#b = input('inserisci un altro numero');

#print(a+b);

#x, y, z = 37, 12, 22;
#print(x);
#print (y);
#print (z);

#WORDLE


import random

def scegli_parola():
    parole = ["python", "computer", "programmazione", "linguaggio", "sviluppatore", "intelligenza", "artificiale"]
    return random.choice(parole)

def gioca_impiccato(parola):
    lunghezza_parola = len(parola)
    lettere_indovinate = ["_"] * lunghezza_parola
    tentativi_rimasti = 10
    lettere_indovinate_corrette = 0
    lettere_indovinate_incorrette = []

    while lettere_indovinate_corrette < lunghezza_parola and tentativi_rimasti > 0:
        print("\nParola:", " ".join(lettere_indovinate))
        print("Tentativi rimasti:", tentativi_rimasti)
        print("Lettere indovinate incorrette:", ", ".join(lettere_indovinate_incorrette))

        lettera = input("Inserisci una lettera: ").lower()

        if len(lettera) != 1 or not lettera.isalpha():
            print("Inserisci solo una lettera.")
            continue

        if lettera in lettere_indovinate_incorrette or lettera in lettere_indovinate:
            print("Hai già provato questa lettera.")
            continue

        if lettera in parola:
            for i in range(lunghezza_parola):
                if parola[i] == lettera:
                    lettere_indovinate[i] = lettera
                    lettere_indovinate_corrette += 1
        else:
            lettere_indovinate_incorrette.append(lettera)
            tentativi_rimasti -= 1

    if lettere_indovinate_corrette == lunghezza_parola:
        print("\nComplimenti! Hai indovinato la parola:", parola)
    else:
        print("\nHai perso! La parola era:", parola)

if __name__ == "__main__":
    print("Benvenuto al gioco dell'impiccato!")
    parola_da_indovinare = scegli_parola()
    gioca_impiccato(parola_da_indovinare)
