#!/bin/python

def find_if_pangram(input):
    alphabet = {}
    for word in input.split():
        word = word.lower()
        for letter in word:
            if letter.isalpha() and letter not in alphabet:
                alphabet[letter] = 1
    if len(alphabet) == 26:
        output = 'pangram'
    else:
        output = 'not pangram'
 
    print output
    return output

def main():
    s = raw_input().strip()
    find_if_pangram(s)

if __name__ == '__main__':
    main()
