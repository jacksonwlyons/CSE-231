##############################################################################
#    Computer Project #4
#
#    Algortithm
#    input cipher text
#    Determine the shift/key for each character in cipher text
#    Determine shift for s and find the most common character
#    Output plain text using shift/key
#    if plain text is readable in english then the program is done
#    if not, loop back through program and try a different shift
#    Repeat until plain text is readable
#
##############################################################################

import string
LETTERS = string.ascii_uppercase
# start of functions
def decode_char(ch,shift):
    '''This function returns the shifted decoding of character ch'''
    if ch not in LETTERS:
        return ch
    elif ch in LETTERS:
        index = LETTERS.find(ch)
        index = (shift + index) % 26
        return LETTERS[index]

def get_shift(s,ignore):
    '''This function returns the shift for string s,
    and the most common character'''
    max_count = 0
    expected_common_char = "E"
    cipher_common_char = ""
    for ch in LETTERS:
        count_s = s.count(ch)
        if count_s > max_count and ch not in ignore:
            cipher_common_char = ch
            max_count = count_s
    shift =LETTERS.find(expected_common_char)-LETTERS.find(cipher_common_char)
        
    return shift, cipher_common_char

def output_plaintext(s,shift):
    ''' Output plain-text of the cipher-text using the shift'''
    outputv = ""
    
    for ch in s:
           outputv += decode_char(ch, shift)
    print()
    print("{:s}".format(outputv.strip()))
    

# main calls the other functions within itself    
def main():
    print("Cracking a Caesar cypher.")
    cipher_txt = input("\nInput cipherText: ").upper()
    ignore = ""
    readable = "no"
    while readable.lower() == "no":
        #cipher_txt = input("\nInput cipherText: ")
        shift, cipher_common_char = get_shift(cipher_txt,ignore)
        output_plaintext(cipher_txt,shift)
        readable = input("\nIs the plaintext readable as English? (yes/no): ")
        print()
        ignore += cipher_common_char
    print("Done.")

    
   
    

# These two lines essentially call the the four functions
if __name__ == "__main__": 
    main()