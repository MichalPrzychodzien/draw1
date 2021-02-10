import random


class WrongScopeError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.start = None
        self.end = None

class Drawings:
    def __init__(self) -> None:
        self.start = int(input("Podaj początek zakresu losowania: "))
        self.end = int(input("Podaj koniec zakresu losowania: "))
        self.chances = int(input("Podaj ilość losowań "))
        self.draw_number = 0
        self.user_number = None
        self.random_number = None


    def drawing1(self):
        random_number = random.randint(self.start, self.end)
        while self.chances > 0:
            self.draw_number += 1
            self.chances -= 1
            try:
                self.user_number = int(input("podaj liczbę do porownania: "))
                if self.user_number > self.end or self.user_number < self.start:
                    raise WrongScopeError()



                if self.user_number == random_number:
                    print(f"Trafiłeś! Wylosowana liczba to {self.user_number}, a trafiłeś za {self.draw_number} razem.")
                    self.chances = 0
                    continue
                elif self.chances > 0:
                    print(f"nie trafiłeś, próbuj dalej. Zostało Ci {self.chances} szanse.")
            except ValueError:
                self.chances += 1
                print(f"Musis podać liczbę z zakresu od {self.start} do {self.end}")
            except WrongScopeError:
                print(f"Twoja liczba wykracza poza zakres od {self.start} do {self.end}, zostały Ci {self.chances} szanse")

        print(f"Koniec szans, frajerze! nie zgadłeś. Szukana liczba to {random_number}")

if __name__ == '__main__':
    lotto = Drawings()
    lotto.drawing1()
