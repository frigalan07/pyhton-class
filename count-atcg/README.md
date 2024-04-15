# Conteo de nucleótidos 'atcg'

El siguiente proyecto toma la necesidad de cuantificar la ocurrencia de cada base nitrogeneda en una secuencia de DNA de interés. 

## Uso

El programa toma esta diseñado para que el usuario digite el nombre del archivo de texto que contiene la secuencia de DNA desde línea de comando, además de que le permite especificar que nucleotidos en específico desea contar. En general, el programa cuenta la ocurrencia de cada una de las bases nitrogenadas.

## Salida

Como datos de salida se mostrará en pantalla la ocurrencia de cada una de las bases 'A', 'T', 'C', 'G'. 
Si se especifíca que nucleótidos desea contar, se mostrará en pantalla la ocurrencia de dichas bases en específico. 
Si no existe el archivo, se muestra un mensaje de error.

## Control de errores

Cuando al programa se le da un archivo que no existe el programa mostrará un mensaje de error, especificando porque no puede funcionar correctamente.

## Pruebas

Hay cuatro casos de prueba: 

Caso de prueba 1:

Descripción: Secuencia válida que contenga una secuencia de DNA 
Datos de entrada: count_atcg.py dna.seq  
Resultado esperado: Ocurrencia de los nucleótidos 

Caso de prueba 2:

Descripción: El archivo no existe
Datos de entrada: count_atcg.py dna.seq  (pero el archivo dna.seq no existe)
Resultado esperado: Mensaje de error, reportando que no existe tal archivo.

Caso de prueba 3:

Descripción: Secuencia que no contenga carácteres válidos 
Datos de entrada: count_atcg.py dna.seq  
Resultado esperado: Verificar que el código ignore los carácteres que no coincidan con las bases nitrogenadas. 

Caso de prueba 4:

Descripción: Conteo de nucleótidos en específico.
Datos de entrada: 
  count_atgc.py dna.seq -n A T
  count_atgc.py dna.seq -nucleotides A T
Resultado esperado: Ocurrencia de los nucleótidos específicados (A T)

Caso de prueba 5: Cuando el archivo esta vacío 
Datos de entrada: count_atcg.py dna.seq  (pero el archivo dna.seq esta vacío)
Resultado esperado: Imprime que la ocurrencia de cada nucleótido es 0. 


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

