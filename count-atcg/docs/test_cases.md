# Casos de prueba o escenarios

Este documento describe los casos de prueba para un script de Python el cual cuenta las ocurrencias de cada nucelótido en una secuencia de DNA. El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.
El script esta diseñado para pedir un archivo desde línea de comandos en formato raw que contiene una secuencia de DNA. Se imprime en pantalla el resultado de ocurrencia de cada uno de los nucelótidos, permite especificar los nucelótidos que se desean contar en específico.  
Se muestra en pantalla mensajes de error si el archivo no existe, esta vacío o tiene carácteres no válidos.
Los casos de prueba tienen como objetivo darle una mayor robustez al programa y que funcione correctamente bajo ciertos condicione de entrada. A continuación se detallan los casos de prueba: 

### Caso de prueba 1: Archivo válido con nucleótidos predeterminados
- python script.py data.txt
- Contenido de data.txt: ATCGATCG
- Resultado esperado: Debería imprimir la frecuencia de cada nucleótido en la secuencia, como por ejemplo:
```python
The number of each nucleotide is:
- Adenine: 2
- Guanine: 2
- Thymine: 2
- Cytosine: 2
```

### Caso de prueba 2: Archivo válido con nucleótidos específicos especificados
- python script.py data.txt -n A T
- Contenido de data.txt: ATCGATCG
- Resultado esperado: Debería imprimir la cantidad de los nucleótidos especificados en la secuencia, como por ejemplo:
```python
The count of each nucleotide is:
Count of Adenines: 2
Count of Thymines: 2
```

### Caso de prueba 3: Archivo válido con nucleótidos inválidos
- python script.py data.txt
- Contenido de data.txt: ATCGXATCG
- Resultado esperado: Debería imprimir un mensaje de error indicando que la secuencia contiene un carácter inválido

### Caso de prueba 4: Archivo vacío
- python script.py empty.txt
- Crear un archivo vacío empty.txt
- Resultado esperado: Debería imprimir un mensaje de error indicando que el archivo está vacío.

### Caso de prueba 5: Archivo no encontrado
- python script.py non_existent_file.txt
- Resultado esperado: Debería imprimir un mensaje de error indicando que no se pudo encontrar el archivo.


FIN

