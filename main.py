def citire_lista():
    list = []
    list_string = input("Dati lista, cu elementele separate prin spatiu: ")
    list_string_split = list_string.split(" ")
    for x in list_string_split:
        list.append(int(x))
    return list


def cautare_numar(list,nr_cautat,pozitie):
    """
    Cauta daca un numar se afla in lista de la o anumita pozitie.
    :param list:lista de numere intregi
    :param nr_cautat:numarul pe care doriti sa il cautati in lista
    :param pozitie: pozitia de la care trebuie sa se caute nr.
    :return: True daca acesta se afla in lista, False in caz contrar
    """
    for i in range(pozitie,len(list)):
        if list[i] == nr_cautat:
            return True
    return False


def test_cautare_numar():
    cautare_numar([2,32,122,12,1456],12,3) is True
    cautare_numar([1,2,3,4,5],4,2) is True
    cautare_numar([2,32,122,12,1456],12,4) is False


def suma_pare(list):
    """
    Determina suma elementelor pare din lista.
    :param list: lista de nr. intregi
    :return: suma nr.
    """
    suma = 0
    for x in list:
        if x % 2 == 0:
            suma = suma + x
    return suma


def test_suma_pare():
    suma_pare([1,2,3,4,5]) == 6
    suma_pare([2,3,12,5,9]) == 14
    suma_pare([1,5,7,11]) == 0


def afisare_pare(list):
    """
    Determina toate elemntele pare din lista si le afiseaza o singura data.
    :param list: lista de nr. intregi
    :return: lista de numere pare afisate o singura data
    """
    result = []
    for x in list:
        if x % 2 == 0 and result.count(x) < 1:
            result.append(x)
    return result

def test_afisare_pare():
    afisare_pare([23,12,3,52,12]) == [12,52]
    afisare_pare([1,3,4,5,4]) == [4]
    afisare_pare([5,10,11,12,10]) == [10, 12]

def lista_inlocuire_el(list):
    """
    Afișați lista obținută prin înlocuirea fiecărui număr cu un tuplu
    :param list: lista de nr. intregi
    :return: lista obținută prin înlocuirea fiecărui număr cu un tuplu
    """
    result = []
    for i in range(len(list)):
        m = False
        for j in range(len(list)):
            if list[j] < list[i] and list[j] != list[i] // 2:
                if not m:
                    for k in range(len(list)):
                        if (list[i] == list[j] + list[k]):
                            if not m:
                                result.append((list[j], list[k]))
                                m = True
        if m is False:
            result.append(list[i])
    return result
def test_lista_inlocuire_el():
    lista_inlocuire_el([4,8,6,3,2,1]) == [(3, 1), (6, 2), (4, 2), (2, 1), 2, 1]
    lista_inlocuire_el([1,2,3,5]) == [1, 2, (2, 1), (3, 2)]
    lista_inlocuire_el([2,3,7,5]) == [2, 3, (2, 5), (3, 2)]

def all_tests():
    test_cautare_numar()
    test_suma_pare()
    test_afisare_pare()
    test_lista_inlocuire_el

def print_Menu():
    print("1. Citire date in lista.")
    print("2. Determinare dacă un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție.")
    print("3. Determinare suma tuturor numerelor întregi pare din lista.")
    print("4. Determina toate numere din lista care sunt pare afisandu-le o singura data.")
    print("5. Afișați lista obținută prin înlocuirea fiecărui număr cu un tuplu.")
    print("x. Iesire")


def main():
    all_tests()
    while True:
        print_Menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            list = []
            list = citire_lista()
        elif optiune == "2":
            numar_cautat = int(input("Dati un nr. pe care doriri sa il cautati: "))
            pozitie_nr = int(input("Dati pozitie: "))
            if cautare_numar(list,numar_cautat,pozitie_nr):
                print("DA")
            else:
                print("NU")
        elif optiune == "3":
            print(suma_pare(list))
        elif optiune == "4":
            print(afisare_pare(list))
        elif optiune == "5":
            print(test_lista_inlocuire_el(list))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Incercati din nou.")


if __name__ == '__main__':
    main()