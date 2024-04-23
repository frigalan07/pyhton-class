# Conteo de nucleótidos 'atcg'

El siguiente proyecto toma la necesidad de cuantificar la ocurrencia de cada base nitrogeneda en una secuencia de DNA de interés. 

## Uso

El programa toma esta diseñado para que el usuario digite el nombre del archivo de texto que contiene la secuencia de DNA desde línea de comando, además de que le permite especificar que nucleotidos en específico desea contar. En general, el programa cuenta la ocurrencia de cada una de las bases nitrogenadas.
Además incluye validaciones en casos donde el archivo no existe, esta vacío o tiene carácteres no válidos 

## Salida

Como datos de salida se mostrará en pantalla la ocurrencia de cada una de las bases 'A', 'T', 'C', 'G'. 
Si se especifíca que nucleótidos desea contar, se mostrará en pantalla la ocurrencia de dichas bases en específico. 
Si no existe el archivo, esta vacío o tiene carácteres no válidos, se muestra un mensaje de error.

## Control de errores

1) *Argumentos inválidos:* Si se proporcionan nucleótidos no válidos en el argumento nucleotides, el script generará una excepción argparse.ArgumentTypeError y mostrará un mensaje de error adecuado.
2) *Archivo no encontrado:* Si el archivo especificado no se puede encontrar, el script generará una excepción IOError y mostrará un mensaje de error indicando que no se pudo encontrar el archivo.
3) *Archivo vacío:* Si el archivo especificado está vacío, el script generará un mensaje de error indicando que el archivo está vacío.
4) *Secuencia con caracteres inválidos:* Si la secuencia de ADN contiene caracteres que no son nucleótidos válidos (A, T, G o C), el script generará una excepción ValueError y mostrará un mensaje de error indicando que la secuencia contiene caracteres inválidos.

## Pruebas

Hay 5 casos de prueba: 

1) Archivo válido con nucleótidos predeterminados:
Se proporciona un archivo de datos válido (data.txt) con la secuencia ATCGATCG.
Se espera que el script cuente la frecuencia de cada nucleótido en la secuencia y los imprima correctamente.

2) Archivo válido con nucleótidos específicos especificados:
Se proporciona un archivo de datos válido (data.txt) con la secuencia ATCGATCG.
Se especifican los nucleótidos A y T para contar.
Se espera que el script cuente la cantidad de Adeninas y Timinas en la secuencia y las imprima correctamente.

3) Archivo válido con nucleótidos inválidos:
Se proporciona un archivo de datos válido (data.txt) con la secuencia ATCGXATCG.
Se espera que el script detecte el carácter inválido X en la secuencia y genere un mensaje de error indicando que la secuencia contiene un carácter inválido.

4) Archivo vacío:
Se crea un archivo vacío (empty.txt).
Se espera que el script detecte que el archivo está vacío y genere un mensaje de error indicando que el archivo está vacío.

5) Archivo no encontrado:
Se especifica un archivo que no existe (non_existent_file.txt).
Se espera que el script genere un mensaje de error indicando que no se pudo encontrar el archivo.


## Datos

Nombre del archivo de texto con una secuencia de DNA en línea de comando. 

  count_atgc.py dna.seq 
  count_atgc.py dna.seq -n A T
  count_atgc.py dna.seq -nucleotides A T


## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución 
o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia MIT License. Consulte el archivo LICENSE para 
obtener más detalles.

## Contáctenos

Si tiene problemas o preguntas, por favor, genera un issue en este repositorio o póngase en contacto 
con nosotros en: frigh@lcg.unam.mx

