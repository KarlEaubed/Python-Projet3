

############################## Nimewo 1 ############################
def get_diksyone():
    diksyone = {
        "kle1": "valè1",
        "kle2": "valè2",
        "kle3": "valè3",
    }
    lis_resulta = []
    for kle, valè in diksyone.items():
        lis_resulta.append([kle, valè])
    print("Lis ak lis valè ak kle yo:", lis_resulta)

get_diksyone()

############################## Nimewo 2 ############################
def get_akolad():
    valè = input("Tape yon valè: ")
    gen_akolad_devan = valè.startswith("{")
    gen_akolad_dèyè = valè.endswith("}")
    if gen_akolad_devan and gen_akolad_dèyè:
        print("Tèks la gen akolad devan ak dèyè.")
    else:
        print("Tèks la pa gen akolad devan ak dèyè.")
    
get_akolad()

############################## Nimewo 3 ############################
def pakouri_dik():
    diksyone = {
        "kle1": "valè1",
        "kle2": "valè2",
        "kle3": "valè3",
    }
    for kle in diksyone:
        print(kle)

pakouri_dik()

############################## Nimewo 4 ############################
def afiche_vale():
    diksyone = {
        "kle1": "valè1",
        "kle2": "valè2",
        "kle3": "valè3",
    }
    for valè in diksyone.values():
        print(valè)

afiche_vale()

############################## Nimewo 5 ############################
diksyone_orijinal = {
    "kle1": "valè1",
    "kle2": "valè2",
    "kle3": "valè3",
}
kopi_diksyone = dict(diksyone_orijinal)
print("Kopi a:", kopi_diksyone)

diksyone_orijinal = {
    "kle1": "valè1",
    "kle2": "valè2",
    "kle3": "valè3",
}
kopi_diksyone = diksyone_orijinal.copy()
print("Kopi a:", kopi_diksyone)


############################## Nimewo 6 ############################
diksyone = {
    "name": "Lub",
    "age": 14,
    "assets": ["laptop", "phone"]
}
for kle, valè in diksyone.items():
    if isinstance(valè, str):
        diksyone[kle] = f"_{valè}_"
print(diksyone)

############################## Nimewo 7 ############################
diksyone = {
    "a": "12",
    "b": "abc",
    "c": "12r",
    "d": "90"
}
nouvo_diksyone = {}
for kle, valè in diksyone.items():
    if valè.isdigit():
        nouvo_diksyone[kle] = valè

print(nouvo_diksyone)

############################## Nimewo 8 ############################
diksyone = {"a": 1, "b": 2}
lis_resulta = [(kle, valè) for kle, valè in diksyone.items()]
print(lis_resulta)

############################## Nimewo 9 ############################
lis_tipl = [("a", 1), ("b", 2)]
diksyone = {}
for kle, valè in lis_tipl:
    diksyone[kle] = valè

# Afiche diksyonè a
print(diksyone)

############################## Nimewo 10 ############################
diksyone1 = {
    "antye": 5,
    "chenn": "Hello",
    "lis": [1, 2, 3],
    "set": {4, 5, 6}
}

diksyone2 = {
    "antye": 7,
    "chenn": " World",
    "lis": [4, 5, 6],
    "set": {7, 8, 9}
}

diksyone_kole = {}

for kle, valè in diksyone1.items():
    if kle in diksyone_kole:
        if isinstance(valè, int):
            diksyone_kole[kle] += valè
        else:
            diksyone_kole[kle] += valè
    else:
        diksyone_kole[kle] = valè
for kle, valè in diksyone2.items():
    if kle not in diksyone_kole:
        diksyone_kole[kle] = valè

print(diksyone_kole)
