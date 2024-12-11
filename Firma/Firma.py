class Firma:
    def __init__(self):
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def get_total_mitarbeiter(self):
        return sum(len(abteilung.mitarbeiter) for abteilung in self.abteilungen)

    def get_total_abteilungsleiter(self):
        return len(self.abteilungen)

    def get_total_abteilungen(self):
        return len(self.abteilungen)

    def get_largest_abteilung(self):
        return max(self.abteilungen, key=lambda a: len(a.mitarbeiter), default=None)

    def get_gender_percentage(self):
        total_mitarbeiter = sum(len(abteilung.mitarbeiter) + 1 for abteilung in self.abteilungen)  # +1 für den Abteilungsleiter
        total_males = sum(1 if abteilung.abteilungsleiter.gender == 'm' else 0 for abteilung in self.abteilungen)
        total_females = sum(1 if abteilung.abteilungsleiter.gender == 'f' else 0 for abteilung in self.abteilungen)

        for abteilung in self.abteilungen:
            total_males += sum(1 for mitarbeiter in abteilung.mitarbeiter if mitarbeiter.gender == 'm')
            total_females += sum(1 for mitarbeiter in abteilung.mitarbeiter if mitarbeiter.gender == 'f')

        percent_male = (total_males / total_mitarbeiter) * 100
        percent_female = (total_females / total_mitarbeiter) * 100

        return percent_female, percent_male


class Abteilung(Firma):
    def __init__(self, name, abteilungsleiter):
        super().__init__()  # Aufruf des Konstruktors der Firma
        self.name = name
        self.abteilungsleiter = abteilungsleiter
        self.mitarbeiter = []  # Liste der Mitarbeiter

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)
        mitarbeiter.abteilung = self.name  # Setze die Abteilung des Mitarbeiters

    def __str__(self):
        return f"Abteilung: {self.name}, Abteilungsleiter: {self.abteilungsleiter.name}, Mitarbeiter: {[mitarbeiter.name for mitarbeiter in self.mitarbeiter]}"

class Mitarbeiter:
    def __init__(self, name, gender, abteilung=None):
        self.name = name
        self.gender = gender  # 'm' for male, 'f' for female
        self.abteilung = abteilung

    def __str__(self):
        return f"{self.name} ({self.abteilung})"

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender, abteilung)

    def __str__(self):
        return f"Abteilungsleiter: {self.name} ({self.abteilung})"


if __name__ == "__main__":
    # Beispiel: Objekte erstellen
    firma = Firma()

    # Abteilung 1 mit Abteilungsleiter und Mitarbeitern
    leiter1 = Abteilungsleiter("Alice", "f", "Abteilung 1")
    abteilung1 = Abteilung("Abteilung 1", leiter1)
    mitarbeiter1 = Mitarbeiter("Bob", "m")
    mitarbeiter2 = Mitarbeiter("Charlie", "m")
    abteilung1.add_mitarbeiter(mitarbeiter1)
    abteilung1.add_mitarbeiter(mitarbeiter2)
    firma.add_abteilung(abteilung1)

    # Abteilung 2 mit Abteilungsleiter und Mitarbeitern
    leiter2 = Abteilungsleiter("David", "m", "Abteilung 2")
    abteilung2 = Abteilung("Abteilung 2", leiter2)
    mitarbeiter3 = Mitarbeiter("Eve", "f")
    mitarbeiter4 = Mitarbeiter("Frank", "m")
    mitarbeiter5 = Mitarbeiter("Grace", "f")
    abteilung2.add_mitarbeiter(mitarbeiter3)
    abteilung2.add_mitarbeiter(mitarbeiter4)
    abteilung2.add_mitarbeiter(mitarbeiter5)
    firma.add_abteilung(abteilung2)

    # Ergebnisse
    print("Anzahl der Mitarbeiter:", firma.get_total_mitarbeiter())
    print("Anzahl der Abteilungsleiter:", firma.get_total_abteilungsleiter())
    print("Anzahl der Abteilungen:", firma.get_total_abteilungen())
    largest_abteilung = firma.get_largest_abteilung()
    if largest_abteilung:
        print("Abteilung mit der größten Mitarbeiterstärke:", largest_abteilung.name)
    percent_female, percent_male = firma.get_gender_percentage()
    print(f"Prozentanteil Frauen: {percent_female:.2f}%")
    print(f"Prozentanteil Männer: {percent_male:.2f}%")

    # Zeige alle Abteilungen und deren Mitglieder
    for abteilung in firma.abteilungen:
        print(abteilung)
