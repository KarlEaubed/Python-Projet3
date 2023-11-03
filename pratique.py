
def get_miniskil():
    text = input("Ekri yon bagay: ")
    miniskil_text = text.lower()
    print(miniskil_text)

get_miniskil()

def get_split():
    text = input("Ekri yon fraz: ")
    split_text = text.split()
    print(split_text)

get_split()

def get_premyemo_majiskil():
    text = input("Ekri yon fraz: ")
    title_text = text.title()
    print(title_text)

get_premyemo_majiskil()

def get_inisyal():
    text = "Nan yon chenn karaktè, rekipere premye lèt chak mo."
    mots = text.split()  # Koupe chenn an nan mo yo
    inisyal = [mo[0] for mo in mots]  # Rekipere premye lèt nan chak mo
    nouvo_chenn = ''.join(inisyal)  # Kreye yon nouvo chenn ak tout inisyal sa yo
    print(nouvo_chenn)  # Afiche nouvo chenn lan

get_inisyal()
