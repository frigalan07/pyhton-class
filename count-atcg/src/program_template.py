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

def count_nucleotides(sequence, nucleotides):
      sequence = sequence.upper() 
      counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in sequence:
        if nucleotide in counts:
            counts[nucleotide] += 1
    if nucleotides:
          selected_nucleotide_counts = {nucleotide: counts[nucleotide] for nucleotide in nucleotides} 
          return selected_nucleotide_counts
    else: 
          return counts

```


# ===========================================================================
# =                            main
# ===========================================================================

```python

def count_nucleotides(sequence, nucleotides):
    sequence = sequence.upper()  # Convertir la secuencia a mayúsculas
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in sequence:
        if nucleotide in counts:
            counts[nucleotide] += 1
    if nucleotides:
        selected_nucleotide_counts = {nucleotide: counts[nucleotide] for nucleotide in nucleotides}
        return selected_nucleotide_counts
    else:
        return counts


def main():
    parser = argparse.ArgumentParser(description="Count nucleotides in a DNA sequence.")
    parser.add_argument("filename", help="Name of the file containing the DNA sequence")
    parser.add_argument("-n", "--nucleotides", nargs="+", help="Nucleotides to count")
    args = parser.parse_args()

    filename = args.filename
    nucleotides = args.nucleotides if args.nucleotides else []

    try:
        with open(filename, 'r') as file:
            sequence = file.read().strip()
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return

    nucleotide_counts = count_nucleotides(sequence, nucleotides)

    if nucleotides:
        print("Contenido de nucleótidos seleccionados en la secuencia:")
        for nucleotide, count in nucleotide_counts.items():
            print(f"{nucleotide}: {count}")
    else:
        print("Contenido de todos los nucleótidos en la secuencia:")
        for nucleotide, count in nucleotide_counts.items():
            print(f"{nucleotide}: {count}")

if __name__ == "__main__":
    main()

```






