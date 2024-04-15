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
- El usuario puede especificar que nucleótidos en especifíco le interesa consultar su ocurrencia.
- Imprime a pantalla los resultados de cada una de las sumas correspondiente a cada letra
- Produce un mensaje de error si el archivo no existe. 

Requisitos no funcionales

- El script deberá estar escrito en python.
- El código deberá ser lo más eficiente que se pueda para tener tiempos de respueta rápidos.


## Análisis y Diseño

Para resolver este problema se utiliza una función que recibe una secuencia de DNA y devuelve un diccionario que contiene el recuento de cada nucleótido, también maneja el caso cuando el usuario digita los nucelótidos en especifico que desea conocer su ocurrencia. Maneja las excepciones para validar el archivo de entrada. 

```
Inicio del programa

Función contar_nucleotidos(secuencia, nucleotidos):
    Convertir la secuencia a mayúsculas
    Inicializar un diccionario de recuentos de nucleótidos con valores iniciales de 0 para 'A', 'C', 'G' y 'T'
    Para cada nucleótido en la secuencia:
        Si el nucleótido está en el diccionario de recuentos:
            Incrementar el recuento del nucleótido en el diccionario
    Si se proporcionan nucleótidos específicos:
        Crear un nuevo diccionario solo con los recuentos de los nucleótidos especificados
        Devolver el nuevo diccionario
    Sino:
        Devolver el diccionario completo de recuentos de nucleótidos

Función principal:
    Parsear los argumentos de línea de comandos
    Leer el nombre del archivo de la secuencia de ADN desde los argumentos
    Leer la secuencia de ADN desde el archivo
    Manejar excepciones:
        Si el archivo no se encuentra, imprimir un mensaje de error y salir del programa
        Si ocurre otro error, imprimir un mensaje de error y salir del programa
    Limpiar la secuencia de ADN eliminando los caracteres de retorno de carro y salto de línea
    Contar los nucleótidos en la secuencia, usando los nucleótidos especificados si se proporcionan
    Imprimir los recuentos de los nucleótidos en la consola

Inicio del programa principal:
    Llamar a la función principal



```

El archivo de entrada deberá estar en formato raw y pasarse por línea de comando, el cual solo deberá contener la secuencia de nucleótidos (A,T,C,G), puede contener otras letras pero estan serán ignoradas. Si las letras son minúsculas, estás son cambiadas a mayúsculas. 
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
- **Descripción**: El actor proporciona un archivo de entrada desde línea de comando, tiene la opción de especificar los nucleótidos en específico cuya ocurrencia quiera determinar. El sistema valida la existencia del archivo. Calcula la ocurrencia de cada una de las bases nitrogenadas. Letras diferentes serán ignoradas y las minúsculas serán convertidas a mayúsculas. 
  
- **Flujo principal**:
        1. El actor inicia el sistema proporcionando el archivo de entrada con la secuencia de DNA, desde línea de comando.
	2. El sistema valida la existencia de el archivo.
	3. El sistema calcula la ocurrencia de cada una de las bases nitrogenadas.
	4. El sistema muestra el resultado.

	
- **Flujos alternativos**:
	 - Si el archivo proporcionado no existe.
    1) El sistema muestra un mensaje de error diciendo que el archivo no se encuentra.
