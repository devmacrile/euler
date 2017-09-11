# -*- coding: utf-8 -*-
"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the 
first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical 
position and adding these values we form a word value. For example, the word value 
for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we 
shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
nearly two-thousand common English words, how many are triangle words?
"""


from eutil import clock


LETTERS = {chr(ucode): (i + 1) for i, ucode in enumerate(range(ord('a'), ord('z') + 1))}

def load_words():
    with open('../../data/words.txt') as f:
        raw_words = f.read()
    words = [w.strip('"').lower() for w in raw_words.split(',')]
    return words

def word_value(word):
    return sum([LETTERS[l] for l in word])

def triangle_number(n):
    """Returns the nth triangle number"""
    return (n * (n  + 1)) // 2

@clock
def main():
    words = load_words()
    values = [word_value(w) for w in words]
    triangle_numbers = set(triangle_number(n) for n in range(1, 25))
    triangle_values = filter(lambda x: x in triangle_numbers, values)
    return len(triangle_values), triangle_values


if __name__ == '__main__':
    main()