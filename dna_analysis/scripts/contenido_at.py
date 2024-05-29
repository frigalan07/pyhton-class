"""
contenido_at: Script para calcular el contenido de adenina y timina en secuencias de ADN.

Este script ayuda a determinar el porcentaje de las bases de adenina (A)
y timina (T) en una secuencia de ADN dada. Esto es útil para estudios genéticos donde
las proporciones de AT pueden ser indicativas de ciertas características genómicas.

Funciones:
- calculate_at_content(sequence, normalize=True): Devuelve el porcentaje de AT en la secuencia.
"""

import argparse
import sys

# Aseguramos que los módulos personalizados se puedan importar
sys.path.append("/Users/frida_galan/Desktop/PythonSEM2/pyhton-class/dna_analysis/utils")
sys.path.append("/Users/frida_galan/Desktop/PythonSEM2/pyhton-class/dna_analysis/operations")

from file_io import read_dna_sequence
from validators import validate_dna_sequence

def calculate_at_content(sequence, normalize=True):
    """
    Calcula el contenido porcentual de adenina (A) y timina (T) en una secuencia de ADN.

    Args:
        sequence (str): La secuencia de ADN a analizar.
        normalize (bool): Si True, normaliza el contenido de AT en caso de que haya 'N's en la secuencia.

    Returns:
        float: El porcentaje de contenido de AT en la secuencia.

    Raises:
        ValueError: Si la secuencia está vacía o contiene caracteres no válidos.
    """
    if not sequence:
        raise ValueError("La secuencia está vacía")
    
    sequence = sequence.upper()
    valid_bases = set("ATGCN")
    
    if any(base not in valid_bases for base in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos")
    
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    at_count = a_count + t_count
    
    if normalize:
        valid_bases_count = sum(sequence.count(base) for base in "ATGC")
        return (at_count / valid_bases_count) * 100 if valid_bases_count > 0 else 0
    else:
        return (at_count / len(sequence)) * 100

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="El siguiente programa calcula el contenido de AT de una secuencia de ADN")

    parser.add_argument("-i", "--input_file", type=str, help="Nombre del archivo a evaluar", required=True)

    args = parser.parse_args()

    # Abrimos la secuencia de ADN con el módulo importado
    try:
        dna_sequence = read_dna_sequence(args.input_file)
    except FileNotFoundError:
        print(f"Error: El archivo '{args.input_file}' no se encontró.")
        sys.exit(1)
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        sys.exit(1)

    # Validamos la secuencia
    try:
        validate_dna_sequence(dna_sequence)
        at_content = calculate_at_content(dna_sequence)
        print(f"El contenido de AT es: {at_content:.2f}%")
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        sys.exit(1)
