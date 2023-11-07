
############################## Nimewo 1 ############################
def retounen_envès(mo):
    envès = mo[::-1]
    return envès

mo_enteresan = "kreye"
mo_envès = retounen_envès(mo_enteresan)
print(mo_envès)

############################## Nimewo 2 ############################
import random
import string

def generate_aleatory_code(n):
    alphabet = string.ascii_letters
    aleyatwa_kòd = ''.join(random.choice(alphabet) for i in range(n))

    return aleyatwa_kòd
kòd_aleyatwa = generate_aleatory_code(8)
print(kòd_aleyatwa)

############################## Nimewo 3 ############################
import random
import string

def generate_unique_aleatory_code(n):
    alphabet = string.ascii_letters

    if n > len(alphabet):
        raise ValueError("N ap mande yon kòd ki pi long pase alfabèt la.")
    aleyatwa_kòd = ''.join(random.sample(alphabet, n))

    return aleyatwa_kòd
kòd_aleyatwa = generate_unique_aleatory_code(8)
print(kòd_aleyatwa)

############################## Nimewo 4 ############################
import random
import string

def generate_unique_alphanumeric_code(n):
    alphanumeric = string.ascii_letters + string.digits

    if n > len(alphanumeric):
        raise ValueError("N ap mande yon kòd ki pi long pase karaktè yo disponib.")
    aleyatwa_kòd = ''.join(random.sample(alphanumeric, n))

    return aleyatwa_kòd
kòd_aleyatwa = generate_unique_alphanumeric_code(8)
print(kòd_aleyatwa)

############################## Nimewo 5 ############################
import re

def generate_slug_from_string(input_string):
    filtered_string = re.sub(r'[^a-zA-Z0-9-]', '-', input_string)
    slug = filtered_string.strip('-')

    return slug

input_chenn = "Ou gen yon lis chenn. Jenere yon SLUG!"
slug = generate_slug_from_string(input_chenn)
print(slug)

############################## Nimewo 6 ############################
def separate_letters_with_hyphen(word):
    letters = list(word)
    hyphen = '-'
    separated_word = hyphen.join(letters)
    
    return separated_word

mo_a_sepere = separate_letters_with_hyphen("kreye")
print(mo_a_sepere)

############################## Nimewo 7 ############################
def encrypt_word(word):
    encrypted_word = '-'.join(str(ord(char.lower()) - ord('a')) for char in word)
    return encrypted_word

mo_kripte = encrypt_word("ALO")
print(mo_kripte)

############################## Nimewo 8 ############################
def decrypt_word(encrypted_word):
    parts = encrypted_word.split('-')
    decrypted_word = ''.join(chr(int(part) + ord('a')) for part in parts)
    return decrypted_word

mo_kripte = "0-11-14"
mo_dekripte = decrypt_word(mo_kripte)
print(mo_dekripte)

############################## Nimewo 9 ############################
def return_both_values(param1, param2):
    return (param1, param2)

valè1 = "premye"
valè2 = "dezyèm"
rezilta = return_both_values(valè1, valè2)
print(rezilta)

############################## Nimewo 10 ############################
def extract_initials(full_name):
    words = full_name.split('-')
    initials = ''.join(word[0].upper() for word in words)
    return initials

non = "Jean-Baptiste Jean"
inisyal = extract_initials(non)
print(inisyal)
