################ Nimewo 1 ############################
def get_miniskil():
    text = input("Ekri yon bagay: ")
    miniskil_text = text.lower()
    print(miniskil_text)

get_miniskil()

################ Nimewo 2 ############################

def get_split():
    text = input("Ekri yon fraz: ")
    split_text = text.split()
    print(split_text)

get_split()

################ Nimewo 3 ############################

def get_premyemo_majiskil():
    text = input("Ekri yon fraz: ")
    title_text = text.title()
    print(title_text)

get_premyemo_majiskil()

################ Nimewo 4 ############################

def get_inisyal():
    text = "Nan yon chenn karaktè, rekipere premye lèt chak mo."
    mots = text.split()  # Koupe chenn an nan mo yo
    inisyal = [mo[0] for mo in mots]  # Rekipere premye lèt nan chak mo
    nouvo_chenn = ''.join(inisyal)  # Kreye yon nouvo chenn ak tout inisyal sa yo
    print(nouvo_chenn)  # Afiche nouvo chenn lan

get_inisyal()

################ Nimewo 5 ############################
def get_ranplase():
    text = input("Antre yon fraz: ")
    replaced_text = text.replace('a', '@')
    print(replaced_text)

get_ranplase()

################ Nimewo 6 ############################
def get_ranvese():
    text = input("Antre yon mo: ")
    first_char = text[0]
    last_chars = text[1:]
    result_text = first_char.upper() + last_chars.lower()
    print(result_text)

get_ranvese()

################ Nimewo 7 ############################
def get_endeks():
    text = input("Antre yon fraz: ")
    index = text.find('a')
    print(index)

get_endeks()

################ Nimewo 8 ############################
def get_totalendeks():
    text = input("Antre yon fraz: ")
    result =text.lower().count("a")
    print(result)

################ Nimewo 9 ############################
def get_min():
    text = input("Antre yon fraz: ")
    result =[i for i, char in enumerate(text) if char == "a"]
    print(result)
    
get_min()

################ Nimewo 10 ############################
def suprime_espas():
    text = input("Antre yon fraz: ")
    result =text.replace(" ", "") + str(len(text) - text.count(" "))
    print(result)
    
suprime_espas()