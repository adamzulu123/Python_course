import itertools
import random

#a) [0,1,0,1,0,...]
def zad7_6_a(): 
    iter_a = 0

    for i in itertools.cycle('01'): 
        if iter_a > 10:
            break
        else: 
            iter_a +=1
            print(i, end=',')

#b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],

def zad7_7_b(): 
    directions = ["N", "E", "S", "W"]

    random_values = [random.choice(directions) for _ in range(10)]
    for i in random_values:
        print(i, end=',')


#c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
def zad7_6_c():
    iter_c = 0; 
    for i in itertools.cycle(range(0,7)): 
        if iter_c > 13: 
            break
        else: 
            print(i, end=",")
            iter_c +=1


#testy
print('a)')
zad7_6_a()
print('\n')

print('b)')
zad7_7_b()
print('\n')

print('c)')
zad7_6_c()
print('\n')