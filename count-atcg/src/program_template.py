'''
NAME
       **Conteo de nucleótidos 'atcg'**

VERSION
        Python 3.12.2

AUTHOR

Frida Galán Hernández

DESCRIPTION
        El siguiente script recibe un archivo de entrada llamado sequence.txt en formato raw y cuenta la ocurrencia de cada uno de los nucelótidos.
        Se imprime a pantalla los resultados o un mensaje de error si el formato del archivo no es correcto o si este no existe.

CATEGORY

        Procesamiento de archivos 

USAGE

    % python count-atcg [sequence.txt]
    

ARGUMENTS
       sequence.txt

METHOD
       Utilización de funciones 

        
'''


# ===========================================================================
# =                            imports
# ===========================================================================
       ```python

open()
print()

```


# ===========================================================================
# =                            Command Line Options
# ===========================================================================

```bash
python3 count-atcg [sequence.txt]

```


# ===========================================================================
# =                            functions
# ===========================================================================

```python

def main():
    try:
        with open('sequence.txt', 'r') as file:
            sequence = file.read().strip()
            if '\r' in sequence or '\n' in sequence:
                raise ValueError("El archivo no está en formato raw.")
    except FileNotFoundError:
        print("El archivo sequence.txt no se encontró.")
        return
    except ValueError as e:
        print("Error:", e)
        return

```


# ===========================================================================
# =                            main
# ===========================================================================

```python

def main():
    try:
        with open('sequence.txt', 'r') as file:
            sequence = file.read().strip()
            if '\r' in sequence or '\n' in sequence:
                raise ValueError("El archivo no está en formato raw.")
    except FileNotFoundError:
        print("El archivo sequence.txt no se encontró.")
        return
    except ValueError as e:
        print("Error:", e)
        return

    nucleotide_counts = count_nucleotides(sequence)

    print("Contenido de nucleótidos en la secuencia:")
    for nucleotide, count in nucleotide_counts.items():
        print(f"{nucleotide}: {count}")

if __name__ == "__main__":
    main()


```






