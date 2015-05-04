"""A repository for various helper functions"""
import numpy as np


def read(file):
    """Reads the given file and returns its lines and the type of program that uses it"""
    with open(file, 'r') as f:
        lines = f.readlines()
    program = check_program(lines)

    return lines, program


def check_program(lines):
    """Takes the lines of an output file and determines what program wrote (or reads) them"""
    programs = {
        '* O   R   C   A *': 'orca',
        'Welcome to Q-Chem': 'qchem',
        'PSI4: An Open-Source Ab Initio Electronic Structure Package': 'psi4',
        'Northwest Computational Chemistry Package (NWChem)': 'nwchem',
        '#ZMATRIX': 'zmatrix',
        '* CFOUR Coupled-Cluster techniques for Computational Chemistry *': 'cfour',
        '***  PROGRAM SYSTEM MOLPRO  ***': 'molpro',
        "----- GAMESS execution script 'rungms' -----": 'gamess'
    }

    program = None
    for line in lines:
        line = line.strip()
        if line in programs:
            program = programs[line]
            break

    return program

short_to_long_names = {
    'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Be': 'Beryllium', 'B': 'Boron', 'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen', 'F': 'Fluorine', 'Ne': 'Neon', 'Na': 'Sodium', 'Mg': 'Magnesium', 'Al': 'Aluminum', 'Si': 'Silicon', 'P': 'Phosphorus', 'S': 'Sulfur', 'Cl': 'Chlorine', 'Ar': 'Argon',
    'K': 'Potassium', 'Ca': 'Calcium', 'Sc': 'Scandium', 'Ti': 'Titanium', 'V': 'Vanadium', 'Cr': 'Chromium', 'Mn': 'Manganese', 'Fe': 'Iron', 'Co': 'Cobalt', 'Ni': 'Nickel', 'Cu': 'Copper', 'Zn': 'Zinc', 'Ga': 'Gallium', 'Ge': 'Germanium', 'As': 'Arsenic', 'Se': 'Selenium', 'Br': 'Bromine', 'Kr': 'Krypton',
    'Rb': 'Rubidium', 'Sr': 'Strontium', 'Y': 'Yttrium', 'Zr': 'Zirconium', 'Nb': 'Niobium', 'Mo': 'Molybdenum', 'Tc': 'Technetium', 'Ru': 'Ruthenium', 'Rh': 'Rhodium', 'Pd': 'Palladium', 'Ag': 'Silver', 'Cd': 'Cadmium', 'In': 'Indium', 'Sn': 'Tin', 'Sb': 'Antimony', 'Te': 'Tellurium', 'I': 'Iodine', 'Xe': 'Xenon',
    'Cs': 'Cesium', 'Ba': 'Barium', 'La': 'Lanthanum', 'Ce': 'Cerium', 'Pr': 'Praseodymium', 'Nd': 'Neodymium', 'Pm': 'Promethium', 'Sm': 'Samarium', 'Eu': 'Europium', 'Gd': 'Gadolinium', 'Tb': 'Terbium', 'Dy': 'Dysprosium', 'Ho': 'Holmium', 'Er': 'Erbium', 'Tm': 'Thulium', 'Yb': 'Ytterbium', 'Lu': 'Lutetium', 'Hf': 'Hafnium', 'Ta': 'Tantalum', 'W': 'Tungsten', 'Re': 'Rhenium', 'Os': 'Osmium', 'Ir': 'Iridium', 'Pt': 'Platinum', 'Au': 'Gold', 'Hg': 'Mercury', 'Tl': 'Thallium', 'Pb': 'Lead', 'Bi': 'Bismuth', 'Po': 'Polonium', 'At': 'Astatine', 'Rn': 'Radon',
    'Fr': 'Francium', 'Ra': 'Radium', 'Ac': 'Actinium', 'Th': 'Thorium', 'Pa': 'Protactinium', 'U': 'Uranium', 'Np': 'Neptunium', 'Pu': 'Plutonium', 'Am': 'Americium', 'Cm': 'Curium', 'Bk': 'Berkelium', 'Cf': 'Californium', 'Es': 'Einsteinium', 'Fm': 'Fermium', 'Md': 'Mendelevium', 'No': 'Nobelium', 'Lr': 'Lawrencium', 'Rf': 'Rutherfordium', 'Db': 'Dubnium', 'Sg': 'Seaborgium', 'Bh': 'Bohrium', 'Hs': 'Hassium', 'Mt': 'Meitnerium', 'Ds': 'Darmstadtium', 'Rg': 'Roentgenium', 'Cp': 'Copernicium', 'Uut': 'Ununtrium', 'Uuq': 'Ununquadium', 'Uup': 'Ununpentium', 'Uuh': 'Ununhexium', 'Uus': 'Ununseptium', 'Uuo': 'Ununoctium'
}
atomic_numbers = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18,
    'K': 19, 'Ca': 20, 'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30, 'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36,
    'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40, 'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47, 'Cd': 48, 'In': 49, 'Sn': 50, 'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54,
    'Cs': 55, 'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60, 'Pm': 61, 'Sm': 62, 'Eu': 63, 'Gd': 64, 'Tb': 65, 'Dy': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70, 'Lu': 71, 'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80, 'Tl': 81, 'Pb': 82, 'Bi': 83, 'Po': 84, 'At': 85, 'Rn': 86,
    'Fr': 87, 'Ra': 88, 'Ac': 89, 'Th': 90, 'Pa': 91, 'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96, 'Bk': 97, 'Cf': 98, 'Es': 99, 'Fm': 100, 'Md': 101, 'No': 102, 'Lr': 103, 'Rf': 104, 'Db': 105, 'Sg': 106, 'Bh': 107, 'Hs': 108, 'Mt': 109, 'Ds': 110, 'Rg': 111, 'Cp': 112, 'Uut': 113, 'Uuq': 114, 'Uup': 115, 'Uuh': 116, 'Uus': 117, 'Uuo': 118,
}

long_to_short_names = {
    'Hydrogen': 'H', 'Helium': 'He', 'Lithium': 'Li', 'Beryllium': 'Be', 'Boron': 'B', 'Carbon': 'C', 'Nitrogen': 'N', 'Oxygen': 'O', 'Fluorine': 'F', 'Neon': 'Ne', 'Sodium': 'Na', 'Magnesium': 'Mg', 'Aluminum': 'Al', 'Silicon': 'Si', 'Phosphorus': 'P', 'Sulfur': 'S', 'Chlorine': 'Cl', 'Argon': 'Ar',
    'Potassium': 'K', 'Calcium': 'Ca', 'Scandium': 'Sc', 'Titanium': 'Ti', 'Vanadium': 'V', 'Chromium': 'Cr', 'Manganese': 'Mn', 'Iron': 'Fe', 'Cobalt': 'Co', 'Nickel': 'Ni', 'Copper': 'Cu', 'Zinc': 'Zn', 'Gallium': 'Ga', 'Germanium': 'Ge', 'Arsenic': 'As', 'Selenium': 'Se', 'Bromine': 'Br', 'Krypton': 'Kr',
    'Rubidium': 'Rb', 'Strontium': 'Sr', 'Yttrium': 'Y', 'Zirconium': 'Zr', 'Niobium': 'Nb', 'Molybdenum': 'Mo', 'Technetium': 'Tc', 'Ruthenium': 'Ru', 'Rhodium': 'Rh', 'Palladium': 'Pd', 'Silver': 'Ag', 'Cadmium': 'Cd', 'Indium': 'In', 'Tin': 'Sn', 'Antimony': 'Sb', 'Tellurium': 'Te', 'Iodine': 'I', 'Xenon': 'Xe',
    'Cesium': 'Cs', 'Barium': 'Ba', 'Lanthanum': 'La', 'Cerium': 'Ce', 'Praseodymium': 'Pr', 'Neodymium': 'Nd', 'Promethium': 'Pm', 'Samarium': 'Sm', 'Europium': 'Eu', 'Gadolinium': 'Gd', 'Terbium': 'Tb', 'Dysprosium': 'Dy', 'Holmium': 'Ho', 'Erbium': 'Er', 'Thulium': 'Tm', 'Ytterbium': 'Yb', 'Lutetium': 'Lu', 'Hafnium': 'Hf', 'Tantalum': 'Ta', 'Tungsten': 'W', 'Rhenium': 'Re', 'Osmium': 'Os', 'Iridium': 'Ir', 'Platinum': 'Pt', 'Gold': 'Au', 'Mercury': 'Hg', 'Thallium': 'Tl', 'Lead': 'Pb', 'Bismuth': 'Bi', 'Polonium': 'Po', 'Astatine': 'At', 'Radon': 'Rn',
    'Francium': 'Fr', 'Radium': 'Ra', 'Actinium': 'Ac', 'Thorium': 'Th', 'Protactinium': 'Pa', 'Uranium': 'U', 'Neptunium': 'Np', 'Plutonium': 'Pu', 'Americium': 'Am', 'Curium': 'Cm', 'Berkelium': 'Bk', 'Californium': 'Cf', 'Einsteinium': 'Es', 'Fermium': 'Fm', 'Mendelevium': 'Md', 'Nobelium': 'No', 'Lawrencium': 'Lr', 'Rutherfordium': 'Rf', 'Dubnium': 'Db', 'Seaborgium': 'Sg', 'Bohrium': 'Bh', 'Hassium': 'Hs', 'Meitnerium': 'Mt', 'Darmstadtium': 'Ds', 'Roentgenium': 'Rg', 'Copernicium': 'Cp', 'Ununtrium': 'Uut', 'Ununquadium': 'Uuq', 'Ununpentium': 'Uup', 'Ununhexium': 'Uuh', 'Ununseptium': 'Uus', 'Ununoctium': 'Uuo'
}


def convert_name(name, s_to_l=True):
    if s_to_l:
        return short_to_long_names[name]
    return long_to_short_names[name]


def atomic_number(name):
    return atomic_numbers[name]


energy_conversions = {
    'hartree': {'hartree': 1, 'kJ/mol': 2625.50, 'kcal/mol': 627.51, 'eV': 27.212, '1/cm': 2.1947e5},
    'kJ/mol': {'hartree': 3.8088e-4, 'kJ/mol': 1, 'kcal/mol': 0.23901, 'eV': 1.0364e-2, '1/cm': 83.593},
    'kcal/mol': {'hartree': 1.5936e-3, 'kJ/mol': 4.1840, 'kcal/mol': 1, 'eV': 4.3363e-2, '1/cm': 349.75},
    'eV': {'hartree': 3.6749e-2, 'kJ/mol': 96.485, 'kcal/mol': 23.061, 'eV': 1, '1/cm': 8065.5},
    '1/cm': {'hartree': 4.5563e-6, 'kJ/mol': 1.1963e-2, 'kcal/mol': 2.8591e-3, 'eV': 1.2398e-4, '1/cm': 1}
}


def convert_energy(data, in_type='hartree', out_type='kcal/mol'):
    if in_type not in energy_conversions or out_type not in energy_conversions[in_type]:
        raise SyntaxError("Unsupported energy type, please use {}".format(list(energy_conversions.keys())))
    conversion = energy_conversions[in_type][out_type]
    
    if isinstance(data, (int, float)):
        return data * conversion
    elif isinstance(data, np.ndarray):
        return data * np.full(data.shape, conversion)
    elif isinstance(data, (list, tuple)):
        try:
            return [conversion * i for i in data]
        except TypeError:
            raise SyntaxError("List may only be filled with numbers.")
    else:
        raise SyntaxError(type(data) + " is not currently supported. Please use int, float, np.ndarray, or list")