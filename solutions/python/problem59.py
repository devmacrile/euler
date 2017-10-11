# -*- coding: utf-8 -*-
"""
Each character on a computer is assigned a unique code and the preferred standard 
is ASCII (American Standard Code for Information Interchange). For example, 
uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. The advantage 
with the XOR function is that using the same encryption key on the cipher text, 
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. The user would keep the encrypted message 
and the encryption key in different locations, and without both "halves", it is 
impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is 
to use a password as a key. If the password is shorter than the message, which is 
likely, the key is repeated cyclically throughout the message. The balance for this 
method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case 
characters. Using cipher.txt, a file containing the encrypted ASCII codes, and the 
knowledge that the plain text must contain common English words, decrypt the message 
and find the sum of the ASCII values in the original text.
"""

import os
import itertools
from collections import Counter
from string import ascii_lowercase

from eutil import clock


def load_codes():
    datapath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data/')
    with open(datapath + 'cipher.txt') as f:
        ascii_codes = f.readline().strip()
    return map(int, ascii_codes.split(','))


def matches_english(text, top=10, thresh=3):
    assert thresh <= 5
    most_common_english = ['the', 'and', 'be', 'of', 'to']
    words = text.split()
    topwords = map(lambda x: x[0], Counter(words).most_common(top))
    common_matches = sum(map(lambda x: x in topwords, most_common_english))
    if common_matches >= thresh:
        return True
    else:
        return False


@clock
def main():
    n = 3
    codes = load_codes()
    lowercase_codes = map(ord, ascii_lowercase)
    for combo in itertools.combinations(lowercase_codes, n):
        # combinations, not permutations, so need an offset
        # representing the permuted key codes
        for offset in range(n):
            keycodes = combo[offset:] + combo[:offset]
            key = keycodes * (len(codes) // n) + keycodes[:len(codes) % n]
            decoded = map(lambda x: x[0] ^ x[1], zip(codes, key))

            text = ''.join(map(chr, decoded))
            if matches_english(text):
                return sum(decoded), text

    return None, 'Failed to decrypt text.'


if __name__ == '__main__':
    main()