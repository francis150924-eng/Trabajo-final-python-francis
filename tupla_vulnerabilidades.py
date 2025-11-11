# Ejemplo: Trabajo con tuplas en Python

# Creación de la tupla
vulnerabilidades = ('SQL Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio')

# Mostrar tupla completa
print("Tupla completa:", vulnerabilidades)

# a) Mostrar el segundo elemento
print("\na) Segundo elemento de la tupla:")
print(vulnerabilidades[1])

# b) Mostrar los dos últimos elementos
print("\nb) Los dos últimos elementos de la tupla:")
print(vulnerabilidades[-2:])

# c) Intentar modificar un elemento (se producirá un error)
print("\nc) Intento de modificar un elemento (esto genera un error porque las tuplas son inmutables):")
try:
    vulnerabilidades[1] = 'XSS'
except Exception as e:
    print("Error:", e)

# Alternativa: convertir la tupla en lista, modificar y volver a tupla
lista = list(vulnerabilidades)
lista[1] = 'XSS'
vulnerabilidades_modificada = tuple(lista)
print("\nTupla modificada a partir de lista:", vulnerabilidades_modificada)


# --- EXPLICACIÓN ---

Las **tuplas** y las **listas** son tipos de estructuras de datos en Python que permiten almacenar varios elementos, 
pero presentan diferencias importantes:

1. **Mutabilidad**:
   - Las tuplas son **inmutables**, lo que significa que sus elementos no se pueden cambiar, agregar o eliminar una vez creadas.
   - Las listas son **mutables**, por lo que puedes modificar, agregar o eliminar elementos fácilmente.

2. **Sintaxis**:
   - Tuplas: se definen con **paréntesis** `()`
     Ejemplo: `tupla = (1, 2, 3)`
   - Listas: se definen con **corchetes** `[]`
     Ejemplo: `lista = [1, 2, 3]`

3. **Uso recomendado**:
   - Usa tuplas cuando los datos **no deban cambiar**, por ejemplo: coordenadas, fechas, configuraciones fijas, etc.
   - Usa listas cuando necesites **modificar o actualizar** los datos durante la ejecución del programa.

4. **Velocidad**:
   - Las tuplas son un poco más **rápidas** que las listas en acceso y recorrido porque son inmutables.

En resumen:
- Tuplas → datos fijos.
- Listas → datos variables.
