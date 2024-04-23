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

#Abrir y leer el archivo
my_file = open(args.data_file, "r")
dna_sequence = my_file.read() #Aplico metodo para leer 
my_file.close() #Cerrar el archivo

nucl_a = dna_sequence.count('A')
nucl_g = dna_sequence.count('G')
nucl_c = dna_sequence.count('C')
nucl_t = dna_sequence.count('T')

#Analizar si el usuario especifíco nucleotidos específicos 
if args.nucleotides:
    print("La cantidad de cada nucleótidos es:")
    for nucleotide in args.nucleotides:
        if nucleotide == "A":
            print("Cantidad de Adeninas:", nucl_a)
        elif nucleotide == "T":
            print("Cantidad de Timinas:", nucl_t)
        elif nucleotide == "C":
            print("Cantidad de Citosinas:", nucl_c)
        elif nucleotide == "G":
            print("Cantidad de Guaninas:", nucl_g)
else:
    print("La frecuencia de los nucleótidos es:\n- Adenina:", nucl_a, "\n- Guanina:", nucl_g, "\n- Timina:", nucl_t, "\n- Citosina:", nucl_c)

```




