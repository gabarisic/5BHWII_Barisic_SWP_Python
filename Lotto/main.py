import random

def ziehe_lottozahlen(versuche):
    ziehungen = []
    häufigkeit = {i: 0 for i in range(46)}

    for _ in range(versuche):
        gezogene_zahlen = random.sample(range(46), 6)
        ziehungen.append(gezogene_zahlen)

        for zahl in gezogene_zahlen:
            häufigkeit[zahl] += 1

    return häufigkeit

def main():
    versuche = 1000

    häufigkeit = ziehe_lottozahlen(versuche)

    print(f"Gesamte Ziehungen: {versuche}")
    print("Häufigkeit der gezogenen Zahlen:")
    for zahl, h in häufigkeit.items():
        print(f"Zahl {zahl}: {h} Mal gezogen")

if __name__ == "__main__":
    main()
