#Adam Nowak

#4.2
def zad3_5(length):
    r = "|" + "".join(["....|" for i in range(length)]) + "\n"
    r += "    ".join((str(i) for i in range(length + 1)))
    return r

def zad3_6(width, height):
    #drawing one row separator and one column separator
    horizontal_lines = "+---" * width + "+"
    vertical_lines = "|   " * width + "|"

    rec = []
    rec.append(horizontal_lines)

    #adding rows created before, depending on the height of the rectangle
    for _ in range(height):
        rec.append(vertical_lines)
        rec.append(horizontal_lines)

    result = ""
    for line in rec:
        result += line + "\n"

    return result

#4.3
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1

    return result

#4.4
def fibonacci(n):
    a, b, i = 1, 1, 2

    while i < n:
        temp = b
        b = a + b
        a = temp
        i += 1

    return b

#4.5
L = list(range(1, 10))

#in place iteratively
def reverse_list_it(L, left, right):
    if left == right:
        return L
    if left > right or left < 0 or right > len(L):
        raise ValueError("invalid arguments")

    while left < right:
        L[left], L[right] = L[right], L[left]
        left+=1
        right-=1
    return L

# recursion and inplace reversing
def reverse_list_rec(L, left, right):
    if left == right:
        return L
    if left > right or left < 0 or right > len(L):
        raise ValueError("invalid arguments")

    L[left], L[right] = L[right], L[left]
    return reverse_list_rec(L, left+1, right-1)


#4.6
seq = [1, 2, [3, 4, [5, 6]], 7, (8, 9)]
'''
tuple - (), list - []
seq example: 1 + 2 then we have a list so we use recursion for list [3, 4, [5, 6]]
1 recursion: 3+4 -> recursion2: 5+6 => 7+11 = 18
3+ 18 = 21 +7 = 28 -> 
recursion 3: 28 + recursion3: 8+9
28+17=45
'''
def sum_seq(sequence):
    total = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            total += sum_seq(i)
        else:
            total += i

    return total


#4.7
seq2 = [1,(2,3),[],[4,(5,6,7)],8,[9]]
seq3 = [[[[3, 4],([(1)])]], 5, 6, ([56])]
'''
extend function -> add list elements to the end of the current list (new_list) 
so after booting the recursion for list or tuple the result list will be 
added to the main one 
'''
def flatten(seqence):
    new_list = []
    for i in seqence:
        if isinstance(i, (list, tuple)):
            new_list.extend(flatten(i))
        else:
            new_list.append(i)

    return new_list





