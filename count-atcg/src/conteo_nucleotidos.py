'''
NAME
       **Conteo de nucleótidos 'atcg'**

VERSION
        Python 3.12.2

AUTHOR

Frida Galán Hernández

DESCRIPTION

      El siguiente script acepta el nombre del archivo con una secuencia de DNA desde línea de comando y te permite especificar 
      que nucleótidos deseas contar con la opción -n o --nucleotides.

CATEGORY

        Procesamiento de archivos de texto y análisis de datos

USAGE

    count_atgc.py dna.seq -n A T
    count_atgc.py dna.seq -nucleotides A T
    

ARGUMENTS
       dna.seq -n A T
       dna.seq -nucleotides A T

METHOD
       Utilización de funciones 

        
'''


# ===========================================================================
# =                            imports
# ===========================================================================
       ```python

import argparse 

```


# ===========================================================================
# =                            Command Line Options
# ===========================================================================

```bash

count_atgc.py dna.seq -n A T
count_atgc.py dna.seq -nucleotides A T

```


# ===========================================================================
# =                            functions
# ===========================================================================

```python

.count()

```


# ===========================================================================
# =                            main
# ===========================================================================

```python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_file",type=str, help="Path donde se encuentra la secuencia que desea analizar")
parser.add_argument("-n","--nucleotides", type=str, default=["A", "T", "C", "G"], nargs="+", help="Elegir nucleótidos especificos a contar")
args = parser.parse_args()

#Verificar el argumento nucleotides 
try:
    for nucleotide in args.nucleotides:
        if nucleotide.upper() not in ['A','T','C','G']:
            raise argparse.ArgumentTypeError(f"The nucleotide '{nucleotide}' is invalid. Only the letters A, T, G, and C are allowed.")
except argparse.ArgumentTypeError as e:
    print("Error:", e)
    exit()

#Abrir y leer el archivo + validaciones 
try: 
    with open(args.data_file, "r") as my_file:
        dna_sequence = my_file.read().upper()  
    if not dna_sequence:  #Checamos si el archivo esta vacío
        print("Sorry, the file is empty")
        exit()
except IOError:  #Checamos si el archivo existe 
    print("Sorry, couldn't find the file")
    exit()

#Verificar si la secuencia contiene caracteres invalidos 
try: 
    for nucleotide in dna_sequence:
        if nucleotide not in ['A', 'T', 'C', 'G']:
            raise ValueError(f"The sequence contains '{nucleotide}', which is an invalid character.")
except ValueError as e:
    print("Error:", e)
    exit()


#Contar nucleótidos 
nucl_a = dna_sequence.count('A')
nucl_g = dna_sequence.count('G')
nucl_c = dna_sequence.count('C')
nucl_t = dna_sequence.count('T')

#Analizar si el usuario especifíco nucleotidos específicos 
if args.nucleotides:
    print("The count of each nucleotide is:")
    for nucleotide in args.nucleotides:
        if nucleotide == "A":
            print("Count of Adenines:", nucl_a)
        elif nucleotide == "T":
            print("Count of Thymines:", nucl_t)
        elif nucleotide == "C":
            print("Count of Cytosines:", nucl_c)
        elif nucleotide == "G":
            print("Count of Guanines:", nucl_g)
else:
    print("The number of each nucleotide present in the sequence is:\n- Adenine:", nucl_a, "\n- Guanine:", nucl_g, "\n- Thymine:", nucl_t, "\n- Cytosine:", nucl_c)
```




