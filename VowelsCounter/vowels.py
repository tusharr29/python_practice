# Vowels in a string counter

string = input("Enter a string to count the number of vowels:")

vowels = "aeiouAEIOU"

count = 0

def overall_count(string):
    count = 0
    for vowels in string:
        if vowels in "aeiouAEIOU":
            count += 1      
    print(f"The number of vowels in the given string is: {count}")

def individual_count(string):
    a = string.count('a') + string.count('A')
    e = string.count('e') + string.count('E')
    i = string.count('i') + string.count('I')
    o = string.count('o') + string.count('O')
    u = string.count('u') + string.count('U')
    print(f"The count of each vowel is: a/A = {a}, e/E = {e}, i/I = {i}, o/O = {o}, u/U = {u}")

method = input("Chose method = 'overall count' or 'individual count' : ")

if method == 'overall count':
    overall_count(string)
else:
    individual_count(string)