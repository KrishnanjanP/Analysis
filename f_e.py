import numpy as np
import re

def read_numbers(formula):
    numbers = []
    regex = r'\d+'
    matches = re.findall(regex, formula)
    for match in matches:
        numbers.append(int(match))
    return numbers

def parse_formula(formula):
    elements = []
    regex = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(regex, formula)
    for match in matches:
        symbol, count = match
        if count == '':
            count = '1'
        elements.append((symbol, int(count)))
    return elements

#formula = "Y1Co1O3"
print("formula of the phase")
formula = str(input())
numbers = read_numbers(formula)
elements = parse_formula(formula)

X_count =  elements[0][1] #* numbers[0]
Co_count = elements[1][1] #* numbers[1]
O_count =  elements[2][1] #* numbers[2]

print(f"X count: {X_count}")
print(f"Co count: {Co_count}")
print(f"O count: {O_count}")

print("Energy of X in Ry")
E_X = float(input())
E_X  = E_X*13.6057039*X_count # eV/atom
E_Co = -298.27028*13.6057039*Co_count # eV/atom
E_O = -40.965*13.6057039*O_count # eV/molecule

# Define the energy per formula unit of the ternary oxide
print("Energy per formula unit of the phase in Ry")
E_XCO = float(input())
E_XCO = (E_XCO*13.6057039-Co_count*1.75) # eV/formula unit

# Calculate the formation energy of the ternary oxide
#print("Number of atom in formula unit")
N = (X_count+Co_count+O_count)
formation_energy = (E_XCO - E_X - E_Co - E_O)/N

print("The formation energy is", formation_energy, "eV/atom")

