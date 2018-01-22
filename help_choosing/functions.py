import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('ksiazki.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()



# pobieranie danych z bazy
def czytajdane():
    """Funkcja pobiera i wyświetla dane z bazy."""
    cur.execute(
        """
        SELECT * FROM fantastyka
        """)
    ksiazki = cur.fetchall()
    for pozycja in ksiazki:
        print(pozycja['id'], pozycja['tytul'], pozycja['bohater'], pozycja['miejsce'])
    print()


def SearchInFantastykaTable(hero, place, time, topic): 
    if hero == "obojętnie":
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE miejsce= ? AND czasy= ? AND  motyw= ?
                        """, ( place, time, topic ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'], pozycja['bohater'], pozycja['miejsce'],pozycja['czasy'],pozycja['motyw'],pozycja['liczba_tomow'])
           print()
    else:
           cur.execute(
                        """
                        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM fantastyka WHERE bohater= ? AND  miejsce= ? AND czasy= ? AND  motyw= ?
                        """, (hero, place, time, topic ))
           ksiazki = cur.fetchall()
           for pozycja in ksiazki:
                print(pozycja['tytul'], pozycja['bohater'], pozycja['miejsce'],pozycja['czasy'],pozycja['motyw'],pozycja['liczba_tomow'])
           print()

        
 

def SearchInPrzygodaTable(hero, place, time, topic):   
    cur.execute(
        """
        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM przygoda WHERE bohater= ? AND  miejsce= ? AND czasy= ? AND  motyw= ? 
        """, (hero, place, time, topic ) )
    ksiazki = cur.fetchall()
    for pozycja in ksiazki:
        print(pozycja['tytul'], pozycja['bohater'], pozycja['miejsce'],pozycja['czasy'],pozycja['motyw'],pozycja['liczba_tomow'])
    print()

def SearchInKryminalTable(hero, place, time, topic):   
    cur.execute(
        """
        SELECT tytul, bohater, miejsce, czasy, motyw, liczba_tomow FROM kryminal WHERE bohater= ? AND  miejsce= ? AND czasy= ? AND  motyw= ? 
        """, (hero, place, time, topic ) )
    ksiazki = cur.fetchall()
    for pozycja in ksiazki:
        print(pozycja['tytul'], pozycja['bohater'], pozycja['miejsce'],pozycja['czasy'],pozycja['motyw'],pozycja['liczba_tomow'])
    print()