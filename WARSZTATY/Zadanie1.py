"""Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 &ndash; 100. Następnie:
​
1. Zadać pytanie: "Zgadnij liczbę" i pobrać liczbę z klawiatury.
2. Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "To nie jest liczba", po czym wrócić do pkt. 1
3. Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "Za mało!", po czym wrócić do pkt. 1.
4. Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "Za dużo!", po czym wrócić do pkt. 1.
5. Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "Zgadłeś!", po czym zakończyć działanie programu.
​
##### Przykład:
```
Zgadnij liczbę: cześć
To nie jest liczba.
Zgadnij liczbę: 50
Za mało!
Zgadnij liczbę: 75
Za dużo!
Zgadnij liczbę: 63
Zgadłeś!
```"""

from random import randint

rndliczba = randint(1,101)
print(rndliczba)


czy_ok = True
while czy_ok:
    try:
        user_input = int(input("Podaj Liczbę: "))

        if user_input == rndliczba:
            print("Zgadłeś!")
            czy_ok = False
        elif user_input < rndliczba:
            print("Za mało")
        else:
            user_input > rndliczba
            print(f"Za dużo")
            
    except (TypeError, ValueError):
        print("Wprowadzony napis nie jest liczbą, spróbuj ponownie")





