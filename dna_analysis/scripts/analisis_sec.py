"""
Programa que calcula la frecuencia de los codones, además de que identifica sitios de restricción

Uso:
    python analisis_sec.py archivo_adn.txt

Argumentos:
    archivo_adn.txt: Nombre del archivo que contiene la secuencia de ADN.

Descripción:
    Este programa lee una secuencia de ADN desde un archivo y busca los sitios de restricción
    para un conjunto de enzimas de restricción definidas en el programa. Los resultados,
    que incluyen las posiciones de los sitios de corte y las enzimas correspondientes,
    se imprimirán en la salida estándar. Calcula la frecuencia de cada codón de tres bases presentes en la secuencia.

Requerimientos:
    La secuencia de ADN debe estar en formato de texto plano y contener solo caracteres
    válidos ('A', 'C', 'G', 'T').

"""

import argparse
import sys

sys.path.append("/Users/frida_galan/Desktop/PythonSEM2/pyhton-class/dna_analysis/utils")
sys.path.append("/Users/frida_galan/Desktop/PythonSEM2/pyhton-class/dna_analysis/operations")

from utils import file_io
from file_io import read_dna_sequence
from validators import validate_dna_sequence
from frecuencia_codones import calculate_codon_frequency
from sitios_restriccion import find_restriction_sites
from sitios_restriccion import ENZIMAS_RESTRICCION


parser = argparse.ArgumentParser(description="El siguiente programa calcula la frecuencia de codones y además buscar sitios de restriccion para una enzima ")

parser.add_argument("-i", "--input_file",
    type = str,
    help = "Nombre del archivo a evaluar")

args = parser.parse_args()

#Abrimos la secuencia de DNA con el modulo importado
dna_sequence = read_dna_sequence(args.input_file)

#Validamos la secuencia 
if (validate_dna_sequence(dna_sequence)):
    #Buscamos sitios de restriccion e imprimimos resultado
    try: 
        restriccion_sites = find_restriction_sites(dna_sequence, ENZIMAS_RESTRICCION)
        print("Sitios de restricción encontrados:")
        for enzyme, positions in restriction_sites.items():
            positions_str = ', '.join(str(pos) for pos in positions)
            print(f"{enzyme}: Posiciones -> {positions_str}")
        
        #Obtenemos la frecuencia de los codones e imprimimos resultado
        frecuencia = calculate_codon_frequency(dna_sequence)
        print(frecuencia)

    except FileNotFoundError:
        print(f"Error: El archivo '{args.file}' no se encontró.")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
    







