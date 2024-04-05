# Conteo de nucleótidos 'atcg'

El siguiente proyecto toma la necesidad de cuantificar la ocurrencia de cada base nitrogeneda en una secuencia de DNA de interés. 

## Uso

El programa toma un archivo que contiene la secuencia de DNA en formato raw, nombrado sequence.txt

## Salida

Como datos de salida se mostrará en pantalla la ocurrencia de cada una de las bases 'A', 'T', 'C', 'G'. 

## Control de errores

Cuando al programa se le da un archivo que no existe, que no contiene el formato adecuado, el programa mostrará un mensaje de error, especificando porque no puede funcionar correctamente.

## Pruebas

Hay cuatro casos de prueba: 

Caso de prueba 1:

Descripción: Secuencia válida en formato raw
Datos de entrada: sequence.txt ATGATCGG
Resultado esperado: Ocurrencia de los nucleótidos A: 2 T: 2 C: 1 G: 3

Caso de prueba 2:

Descripción: Secuencia con caracteres no válidos
Datos de entrada: sequence.txt ATGATCXG
Resultado esperado: Mensaje de error reportando que tiene caracteres no válidos.

Caso de prueba 3:

Descripción: Secuencia que no esta en formato raw.
Datos de entrada: Archivo sequence.txt (que no esta en formato raw)
Resultado esperado: Mensaje de error, reportando que el formato del archivo no es correcto

Caso de prueba 4:

Descripción: Comprobación de la existencia del archivo.
Datos de entrada: sequence.txt (dicho archivo no existe).
Resultado esperado: Mensaje de error, reportando que no existe tal archivo.


## Datos

Archivo con una secuencia de DNA en formato raw, nombrada 'sequence.txt'


## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución 
o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia [nombre de la licencia]. Consulte el archivo LICENSE para 
obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [información de citación].

## Contáctenos

Si tiene problemas o preguntas, por favor, genera un issue en este repositorio o póngase en contacto 
con nosotros en: [información de contacto].

