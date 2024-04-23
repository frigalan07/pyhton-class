# Conteo de nucleótidos 'atcg'
Fecha: 14/03/2024

**Participantes**:

- Frida Galán Hernández : fridagh@lcg.unam.mx

## Descripción del Problema

El siguiente código cuenta las ocurrencias de los nucléotidos adenina, timina, citocina y guanina en una secuencia de DNA dada. Lo anterior surge de la necesidad de poder cuantificar el contenido de cada base nitrogenada de una secuencia de interés.


## Especificación de Requisitos

Requisitos funcionales

- Lee una secuencia de letras 'A', 'T', 'C', 'G' las cuales corresponden a una base nitrogenada.
- El nombre del archivo es pedido por línea de comando.
- Calcula la ocurrencia de cada una de las bases en toda la secuencia de interés.
- El usuario puede especificar que nucleótidos en especifíco le interesa consultar su ocurrencia y muestra mensaje de error si el nucleótido especificado no es valido.
- Imprime a pantalla los resultados de cada una de las sumas correspondiente a cada letra
- Produce un mensaje de error si el archivo no existe, si esta vacío, si tiene carácteres inválidos. 


Requisitos no funcionales

- El script deberá estar escrito en python.
- El código deberá ser lo más eficiente que se pueda para tener tiempos de respueta rápidos.


## Análisis y Diseño

El script cuenta las ocurrencia de cada nucléotido en una secuencia de DNA y las imprime a pantalla. El usuario da el nombre del archivo por la terminal y puede especificar que nucleotidos en específico desea conocer la ocurrencia, utilizando argumentos posicionales, de lo contrario imprime la frecuencia de todos los nucleótidos. Cuenta con validaciones para: argumentos no válidos, archivos no existentes o vacios y archivos con carácteres no válidos. 


```
1. Importar el módulo argparse

2. Definir un analizador de argumentos usando argparse:
    a. Agregar un argumento para el archivo de datos de la secuencia ("data_file").
    b. Agregar un argumento opcional para los nucleótidos específicos a contar ("nucleotides").

3. Verificar el argumento "nucleotides" para asegurarse de que solo contenga nucleótidos válidos:
    a. Iterar sobre cada nucleótido en los argumentos nucleotides.
    b. Si un nucleótido no es válido (no es A, T, G o C), generar una excepción argparse.ArgumentTypeError.

4. Abrir y leer el archivo de datos de la secuencia:
    a. Intentar abrir el archivo en modo lectura.
    b. Leer el contenido del archivo y convertirlo a mayúsculas.
    c. Si el archivo está vacío, imprimir un mensaje de error y salir del programa.
    d. Si el archivo no se puede encontrar, imprimir un mensaje de error y salir del programa.

5. Verificar si la secuencia contiene caracteres inválidos:
    a. Iterar sobre cada nucleótido en la secuencia de ADN.
    b. Si un nucleótido no es válido (no es A, T, G o C), generar una excepción ValueError.

6. Contar la frecuencia de cada nucleótido en la secuencia de ADN.

7. Imprimir los resultados:
    a. Si se especificaron nucleótidos específicos, imprimir la cantidad de cada uno.
    b. Si no se especificaron nucleótidos, imprimir la frecuencia de cada nucleótido en la secuencia.

8. Fin del programa.

```

El archivo de entrada deberá estar en formato raw y pasarse por línea de comando, el cual solo deberá contener la secuencia de nucleótidos (A,T,C,G). Si las letras son minúsculas, estás son cambiadas a mayúsculas. 
Como salida, solo se mostará en pantalla el número de ocurrencia de cada base, de todas o de las específicadas. Mensajes de error también se imprimirá en pantalla.


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
- **Descripción**: El actor proporciona un archivo de entrada desde línea de comando, tiene la opción de especificar los nucleótidos en específico cuya ocurrencia quiera determinar. El sistema valida la existencia del archivo, que no este vació o que no contenga carácteres . Calcula la ocurrencia de cada una de las bases nitrogenadas.
  
- **Flujo principal**:
1) **Argumentos de línea de comandos:** El programa recibe argumentos de línea de comandos utilizando el módulo argparse. Los argumentos incluyen la ruta al archivo de datos de la secuencia y, de manera opcional, los nucleótidos específicos a contar.
2) **Validación de argumentos:** Se verifica la validez del argumento opcional nucleotides para asegurarse de que solo contenga nucleótidos válidos (A, T, G o C).
3) **Lectura del archivo:** Se intenta abrir y leer el archivo de datos de la secuencia. Si el archivo no puede abrirse o leerse, se maneja la excepción IOError. Si el archivo está vacío, se imprime un mensaje de error y el programa sale.
4) **Procesamiento de la secuencia:** Se lee la secuencia de ADN del archivo y se convierte a mayúsculas. Luego, se verifica si la secuencia de ADN contiene caracteres inválidos. Si se encuentra algún carácter inválido (que no sea A, T, G o C), se maneja la excepción ValueError.
5) **Conteo de nucleótidos:** Se cuentan las ocurrencias de cada nucleótido en la secuencia de ADN.
6) **Impresión de resultados:** Se imprimen los resultados. Si se especificaron nucleótidos específicos, se imprime la cantidad de cada uno. Si no se especificaron nucleótidos, se imprime la frecuencia de cada nucleótido en la secuencia.
7) **Fin del programa:** El programa termina su ejecución.

	
- **Flujos alternativos**:
	 - Si el archivo proporcionado no existe, esta vacío o contiene elementos inválidos:
    1) El sistema muestra un mensaje de error 
