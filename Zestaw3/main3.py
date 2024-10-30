#Adam Nowak
"""
ZAD 3.1
Jest to kod, który sie wykona i zwróci wartość, jednak stosowanie
średnikow w pythonie jest niepotrzebne.
W drugim kodzie każda z tych operacji powinna byc wykonywana w odzielnej
linijce.
W trzecim też operacja print powinna byc nowej linii.


ZAD 3.2
L = L.sort() - zwróci nic, bo sort() sortuje w miejscu, wiec trzeba: L.sort().
x, y = 1, 2, 3 - za duzo wartosci za mało zmiennych
X = 1, 2, 3 ; X[1] = 4 - brak ";" i X[1] w kolejnej linii
X = [1, 2, 3] ; X[3] = 4 - to samo co wyżej plu próbujemy odwołac sie do
indexu, ktory nawet nie istnieje.
X = "abc" ; X.append("d") - nie ma funkcji .apppend() dla typu str.
L = list(map(pow, range(8))) - brakuje argumentow potegi i wykładnika
 i funkcji anonimowej lambda.
"""


#ZAD 3.3
def zad3():
    print("ZAD3")
    print([i for i in range(0, 30) if i % 3 == 0])
    print("\n\n")


#ZAD 3.4
def zad4():
    print("ZAD4")
    while True:
        i = input("Add real number (liczbe rzeczywista): ")
        if i == "stop":
            break
        try:
            x = float(i)
            print(x)
            print(x ** 3)
        except ValueError:
            print("Not real number")

    print("\n\n")

#ZAD3.5
def zad5(length):
    r = "|" + "".join(["....|" for i in range(length)]) + "\n"
    r += "    ".join((str(i) for i in range(length + 1)))
    print(r)
    print("\n\n")


#zad5(10) - use example

#ZAD6
def zad6(width, height):
    #drawing one row separator and one column separator
    horizontal_lines = "+---" * width + "+"
    vertical_lines = "|   " * width + "|"

    rec = []
    rec.append(horizontal_lines)

    #adding rows created before, depending on the height of the rectangle
    for _ in range(height):
        rec.append(vertical_lines)
        rec.append(horizontal_lines)

    #drawing rectangle
    for line in rec:
        print("".join(line))

    print("\n\n")
#zad6(3,2)


#ZAD7
'''
Wykomendowane __str__(): Time(12) Time(3456)
                        [Time(12), Time(3456)]
                        
Wykomendowane __repr__(): 12 sec 3456 sec
[<__main__.Time object at 0x1123d6540>, <__main__.Time object at 0x1123d6510>]
 - dzieje sie tak bo python korzysta z ogolnej reprezentacji klasy object. 
'''


#ZAD8
def zad8():
    a = "b8wa3ct4he9sg15qz12nkl6"
    b = "v1pq5oc3ra2bg76j0s4ht12"

    set1 = set(a)
    set2 = set(b)

    print(list(set1.intersection(set2)))
    print(list(set1.union(set2)))


#ZAD9
def zad9():
    seq = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
    el_sum = []
    for i in seq:
        el_sum.append(sum(i))

    print(el_sum)


#ZAD10
def zad10(number):
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_num = 0

    for i in range(len(number)):
        #checking if we have to subtract or add a number
        if i < len(number) - 1 and rom[number[i]] < rom[number[i+1]]:
            int_num -= rom[number[i]]
        else:
            int_num += rom[number[i]]

    return int_num

#print(zad10("VL"))


