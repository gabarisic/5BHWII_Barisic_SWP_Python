# Falsche Reihenfolgen (auskommentiert, da sie einen SyntaxError verursachen würden):
# def falsch1(**kwargs, *args):  # SyntaxError: **kwargs darf nicht vor *args stehen
#     pass
#
# def falsch2(**kwargs, a, b):  # SyntaxError: **kwargs darf nicht vor statischen Parametern stehen
#     pass

# Beispiel 1: Alle Optionen in einer Funktion
def demo_all(a, b, *args, c="Standard_C", d="Standard_D", **kwargs):
    """
    a, b           : Statische (Positions-)Parameter
    *args          : Zusätzliche Positionsargumente
    c, d           : Keyword-only Parameter (nach *args, können nur als benannte Argumente übergeben werden)
    **kwargs       : Zusätzliche benannte Argumente
    """
    print("Demo All:")
    print("  Statische Parameter: a =", a, ", b =", b)
    print("  *args:", args)
    print("  Keyword-only Parameter: c =", c, ", d =", d)
    print("  **kwargs:", kwargs)
    print("-" * 40)

# Beispiel 2: Nur *args als Parameter
def demo_args(*args):
    """
    Nimmt beliebig viele Positionsargumente entgegen.
    """
    print("Demo Args:")
    print("  *args:", args)
    print("-" * 40)

# Beispiel 3: Nur **kwargs als Parameter
def demo_kwargs(**kwargs):
    """
    Nimmt beliebig viele benannte Argumente entgegen.
    """
    print("Demo kwargs:")
    print("  **kwargs:", kwargs)
    print("-" * 40)

# Beispiel 4: Kombination aus statischen Parametern, *args und **kwargs mit einem erzwungenen Keyword-only Parameter
def demo_mixed(a, *args, b, **kwargs):
    """
    a      : Statischer Parameter
    *args  : Zusätzliche Positionsargumente
    b      : Keyword-only Parameter (muss als benannter Parameter übergeben werden)
    **kwargs: Zusätzliche benannte Argumente
    """
    print("Demo Mixed:")
    print("  Statischer Parameter a:", a)
    print("  *args:", args)
    print("  Keyword-only Parameter b:", b)
    print("  **kwargs:", kwargs)
    print("-" * 40)

def main():
    print("Beispiel 1: demo_all")
    # Aufruf von demo_all mit:
    #   - a, b als Positionsparameter
    #   - weitere Positionsargumente in *args
    #   - c und d als Keyword-only Parameter
    #   - zusätzliche Keywordargumente in **kwargs
    demo_all(1, 2, 3, 4, 5, c="Wert_C", d="Wert_D", extra1="Zusatz_1", extra2="Zusatz_2")

    print("Beispiel 2: demo_args")
    # Aufruf von demo_args nur mit Positionsargumenten:
    demo_args("Alpha", "Beta", "Gamma")

    print("Beispiel 3: demo_kwargs")
    # Aufruf von demo_kwargs nur mit benannten Argumenten:
    demo_kwargs(erste=10, zweite=20, dritte=30)

    print("Beispiel 4: demo_mixed")
    # Aufruf von demo_mixed:
    # a wird als Positionsparameter übergeben.
    # b MUSS als Keyword-Argument übergeben werden.
    # *args fängt weitere Positionsargumente ab.
    # **kwargs sammelt zusätzliche benannte Argumente.
    demo_mixed(100, "X", "Y", b="Z", extra="Extra_Wert")

if __name__ == "__main__":
    main()
