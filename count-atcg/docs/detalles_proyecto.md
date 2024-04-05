# Conteo de nucleótidos 'atcg'
Fecha: 04/03/2024

**Participantes**:

- Frida Galán Hernández : fridagh@lcg.unam.mx

## Descripción del Problema

El siguiente código cuenta las ocurrencias de los nucléotidos adenina, timina, citocina y guanina en una secuencia de tipo raw dada. Lo anterior surge de la necesidad de poder cuantificar el contenido de cada base nitrogenada de una secuencia de interés.


## Especificación de Requisitos

Requisitos funcionales

- Lee una secuencia de letras 'A', 'T', 'C', 'G' las cuales corresponden a una base nitrogenada. 
- Calcula la ocurrencia de cada una de las bases en toda la secuencia de interés.
- Imprime a pantalla los resultados de cada una de las sumas correspondiente a cada letra
- Produce un mensaje de error si el archivo no esta en formato raw.
- Produce un mensaje de error si el archivo no existe. 

Requisitos no funcionales

- El script deberá estar escrito en python.
- El código deberá ser lo más eficiente que se pueda para tener tiempos de respueta rápidos.


## Análisis y Diseño

Para resolver este problema se utiliza una función que recibe una secuencia de DNA y devuelve un diccionario que contiene el recuento de cada nucleótido. Maneja las excepciones para validar el archivo de entrada.

```
Función contar_nucleótidos(secuencia):
    // Inicializar un diccionario para contener los conteos de cada nucleótido
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    // Iterar sobre cada nucleótido en la secuencia
    Para cada nucleótido en secuencia:
        // Verificar si el nucleótido está presente en el diccionario de conteo
        Si nucleótido está en counts:
            // Incrementar el contador para ese nucleótido
            counts[nucleótido] += 1

    // Devolver el diccionario de conteo
    Devolver counts


Función principal:
    Intentar:
        // Abrir el archivo de secuencia y leer la secuencia de ADN
        Abrir 'sequence.txt' en modo lectura como archivo:
            Leer toda la secuencia de ADN del archivo
            Limpiar cualquier espacio en blanco alrededor de la secuencia

            // Verificar si la secuencia contiene caracteres de nueva línea
            Si '\r' está en secuencia o '\n' está en secuencia:
                Lanzar un ValueError indicando que el archivo no está en formato raw

    Capturar FileNotFoundError:
        Imprimir "El archivo sequence.txt no se encontró."
        Terminar la ejecución
    Capturar ValueError como e:
        Imprimir "Error:", e
        Terminar la ejecución

    // Contar los nucleótidos en la secuencia de ADN
    conteos_nucleótidos = contar_nucleótidos(secuencia)

    // Imprimir los resultados
    Imprimir "Contenido de nucleótidos en la secuencia:"
    Para cada nucleótido, conteo en conteos_nucleótidos:
        Imprimir nucleótido, conteo

```

El archivo de entrada deberá estar en formato raw, en un archivo llamado sequence.txt, el cual solo deberá contener la secuencia de nucleótidos (A,T,C,G). Como salida, solo se mostará en pantalla el número de ocurrencia de cada base. Mensajes de error también se imprimirá en pantalla.


#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-------+-------+
         |   Conteo de   |
         |  nucleótidos  |
         |    en una     |
         |  secuencia de |
         |      DNA      |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**: El actor proporciona un archivo de entrada con la secuencia de interés. El sistema valida la existencia del archivo y el que el formato del archivo sea el correcto. Calcula la ocurrencia de cada una de las bases nitrogenadas.
  
- **Flujo principal**:
        1. El actor inicia el sistema proporcionando el archivo de entrada con la secuencia de DNA.
	2. El sistema valida la existencia y formato de el archivo.
	3. El sistema calcula la ocurrencia de cada una de las bases nitrogenadas.
	4. El sistema muestra el resultado.

	
- **Flujos alternativos**:
	 - Si el archivo proporcionado no existe.
    1) El sistema muestra un mensaje de error diciendo que el archivo no se encuentra.
	- Si los datos de entrada no es una secuencia en formato raw.
   1) El sistema muestra un mensaje de error el formato del archivo no es el correcto. 
