#Autor: Adam Nowak

line = """The sun sets quietly over the distant hills,
Whispers of the wind dance through the trees,
A lone bird sings its song to the fading light,
As stars begin to shimmer in the midnight sky. GvR."""


#2.10
'''
split returns a list of elements. delimiter is none, same as maxsplit, so every word in the string separteted 
by whitespace will we added to the list. 
len function returns the length of the list. 
'''
words = line.split()
num_of_el = len(words)
print("2.10 exercise:")
print(num_of_el)


#2.11
'''
first of all we separate letters are create a list of them
then use join function to join the list with "_" string. 
'''
word = "python"
letters_in_word = [x for x in word]
devided_word = "_".join(letters_in_word)
print("\n2.11 exercise:")
print(devided_word)


#2.12
'''
In the beginning I purge elements of the list form ',' and '.'.
Then we iterate through elements and add first and last indication of each word to 
particular list. Then join function to join elements of the lists.
'''
words_cleaned = [word.strip(',.') for word in words]
first_letters = []
last_letters = []

for x in words_cleaned:
    first_letters.append(x[:1])
    last_letters.append(x[-1])


print("\n2.12 exercise:")
print("Word from first indication of each word in line string:")
print(''.join(first_letters))
print("Word from last indication of each word in line string:")
print(''.join(last_letters))


#2.13
'''
using sum function to sum up length of each word in the line string. 
'''
sum_of_words_len = sum(len(word) for word in words_cleaned)

print("\n2.13 exercise:")
print(sum_of_words_len)


#2.14
'''
I use max function and key parameter to determine a function based on which max function 
will find the max character. 
'''
longest_word = max(words_cleaned, key=len)

print("\n2.14 exercise:")
print(longest_word)
print("longest word length: ", len(longest_word))


#2.15
'''
using join method and str function to convert elements of the list to str and the join them.
'''
L = [12, 34, 56, 78, 90, 13, 69, 420, 1, 6, 169]

number_string = ''.join([str(x) for x in L])
print("\n2.15 exercise:")
print(number_string)


#2.16
replaced_line = line.replace("GvR","Guido van Rossum")

print("\n2.16 exercise:")
print(replaced_line)

#2.17
sorted_line_alph = sorted(words_cleaned, key=str.lower)
sorted_line_len = sorted(words_cleaned, key=len)

print("\n2.17 exercise:")
print(sorted_line_alph)
print(sorted_line_len)

#2.18
'''
using str func to convert number, then count func to how many times '0' appears.
'''
number = 10042033660001800
number_of_zeros = str(number).count('0')
print("\n2.18 exercise:")
print(number_of_zeros)

#2.19
'''
First of all we convert number in L to string.
Ten use zfill method to fill elements with zeros, where it's necessary. 
'''
L_str_list = [str(x) for x in L]
L_str_list_completed = [i.zfill(3) for i in L_str_list]
print("\n2.19 exercise:")
print("".join(L_str_list_completed))



