import numpy as np
import random 

word = "FSIIECTF{mi55ing_c0d3_ch4ll3ng3}"

# Convertir chaque caractère en code ASCII
excluded_values = [ord(char) for char in word]

def generate_subarray(excluded_value):
    numbers = [i for i in range(256) if i != excluded_value]
    random.shuffle(numbers) 
    return numbers

sub_list = [generate_subarray(val) for val in excluded_values]

filename = "enc.txt"

# Création des sous-tableaux dans le fichier
with open(filename, 'w') as file:
    file.write("[")
    for idx, subarray in enumerate(sub_list, start=1):
        file.write(f"{subarray},")
    file.seek(file.tell() - 1)
    file.write("]")
