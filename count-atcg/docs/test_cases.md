# Casos de prueba o escenarios

Este documento describe los casos de prueba para un script de Python el cual cuenta las ocurrencias de cada nucelótido en una secuencia de DNA. El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.
El script esta diseñado para pedir un archivo desde línea de comandos en formato raw que contiene una secuencia de DNA. Se imprime en pantalla el resultado de ocurrencia de cada uno de los nucelótidos, permite especificar los nucelótidos que se desean contar en específico.  
Se muestra en pantalla mensajes de error si el archivo no existe.
Los casos de prueba tienen como objetivo darle una mayor robustez al programa y que funcione correctamente bajo ciertos condicione de entrada. A continuación se detallan los casos de prueba: 

### Caso de prueba 1: 

- Descripción: Secuencia válida que contenga una secuencia de DNA 
- Datos de entrada: count_atcg.py dna.seq
- Resultado esperado: Deberá contar correctamenta los nucleótidos y deberá mostrar a pantalla la ocurrencia de los nucleótidos

### Caso de prueba 2: 

- Descripción: El archivo no existe
- Datos de entrada: count_atcg.py dna.seq (pero el archivo dna.seq no existe)
- Resultado esperado: Mensaje de error, reportando que no existe tal archivo.

### Caso de prueba 3: 

- Descripción: Secuencia que no contenga carácteres válidos
- Datos de entrada: count_atcg.py dna.seq
- Resultado esperado: Verificar que el código ignore los carácteres que no coincidan con las bases nitrogenadas.

### Caso de prueba 4: 

- Descripción: Conteo de nucleótidos en específico.
- Datos de entrada:
        count_atgc.py dna.seq -n A T
        count_atgc.py dna.seq -nucleotides A T
- Resultado esperado: Ocurrencia de los nucleótidos específicados (A T)

### Caso de prueba 5: 

- Descripción: Cuando el archivo esta vacío
- Datos de entrada: count_atcg.py dna.seq (pero el archivo dna.seq esta vacío)
- Resultado esperado: Imprime que la ocurrencia de cada nucleótido es 0.


FIN

