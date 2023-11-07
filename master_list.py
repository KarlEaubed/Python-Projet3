
######################### Nimewo 1 #############################
def list_divizib():
    n = 10
    lis_divizib_pa_de = [x for x in range(n+1) if x % 2 == 0]
    print(lis_divizib_pa_de)

list_divizib()

######################### Nimewo 2 #############################
lis_antye = [1, 2, 3, 4, 5]
lis_chenn = [str(x) for x in lis_antye]
print(lis_chenn)

######################### Nimewo 3 #############################
lis_miniskil = ["pom", "kiwi", "zoranj", "fraise"]
lis_majiskil = [x.upper() for x in lis_miniskil]
print(lis_majiskil)

######################### Nimewo 4 #############################
lis_done = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nouvo_lis = [lis_done[i] for i in range(len(lis_done)) if i % 3 == 0]
print(nouvo_lis)

######################### Nimewo 5 #############################
lis_done = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nouvo_lis = [(lis_done[i], lis_done[i + 1], lis_done[i + 2]) for i in range(0, len(lis_done), 3)]
print(nouvo_lis)

######################### Nimewo 6 #############################
lis_avek_doublon = [1, 2, 2, 3, 4, 4, 5, 6, 6]
lis_sans_doublon = list(set(lis_avek_doublon))
print(lis_sans_doublon)

######################### Nimewo 7 #############################
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
nouvo_lis = [x for x in lis1 if x in lis2]
print(nouvo_lis)

######################### Nimewo 8 #############################
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
nouvo_lis = [x for x in lis1 if x not in lis2] + [x for x in lis2 if x not in lis1]
print(nouvo_lis)

######################### Nimewo 9 #############################
diksyone = {"kle1": "valè1", "kle2": "valè2", "kle3": "valè3"}
lis_kle = list(diksyone.keys())
lis_valè = list(diksyone.values())
print("Liste des clés:", lis_kle)
print("Liste des valeurs:", lis_valè)

######################### Nimewo 10 #############################
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis3 = [5, 6, 7, 8, 9]

set1 = set(lis1)
set2 = set(lis2)
set3 = set(lis3)

rejwenn_set = set1.intersection(set2, set3)
rezilta = list(rejwenn_set)
print(rezilta)
