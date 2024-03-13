# Script Verificador de Palíndromos

## Descripción General
Este script define una clase `Palindromo` que verifica si una cadena dada es un palíndromo. Un palíndromo es una palabra, frase, número u otra secuencia de caracteres que se lee igual hacia adelante que hacia atrás, ignorando espacios, puntuación y mayúsculas.

## Características
- **Validación de Palíndromos**: El método de clase `esPalindromo` permite verificar si una cadena es un palíndromo.
- **Prueba de Instancia**: El método `test` de instancia se puede usar para verificar si la cadena asociada con una instancia de clase es un palíndromo.
- **Conversión Automática a Mayúsculas**: Al eliminar una instancia de `Palindromo`, la cadena asociada con ella se imprime en mayúsculas.

## Uso

### Importar la Clase
Primero, asegúrate de incluir la clase `Palindromo` en tu proyecto importándola desde el archivo del script.

### Verificar Palíndromos
Para verificar si una cadena es un palíndromo, puedes llamar directamente al método de clase `esPalindromo` sin necesidad de crear una instancia:

```python
print(Palindromo.esPalindromo('radar'))  # True
print(Palindromo.esPalindromo('sonar'))  # False
```

# Clase A y Sus Métodos

## Descripción General
Este script define una clase `A` que implementa dos métodos principales: uno para devolver la instancia actual de la clase y otro para devolver la longitud de un iterable pasado como argumento. Adicionalmente, el script incluye una función `main` que demuestra el uso de estos métodos.

## Características
- **Retorno de Instancia Actual**: El método `z` devuelve la propia instancia de la clase `A` en la que se invoca.
- **Longitud de un Iterable**: El método `y` recibe un iterable `t` y devuelve su longitud.
- **Demostración de Uso**: La función `main` ilustra varios casos de uso de la clase `A`, incluyendo comparaciones de instancias y el paso de diferentes tipos de iterables a `y`.

## Uso

### Creación de Instancias y Llamadas a Métodos
- Para crear una instancia de la clase `A` y utilizar sus métodos:
```python
a = A()
```

# Sistema de Registro de Logger

## Descripción
Este script contiene una implementación básica de un sistema de registro (`Logger`) diseñado para mantener un registro de mensajes en un archivo. Se incluye también una clase de prueba (`Test`) que demuestra cómo utilizar el `Logger` para registrar mensajes.

## Características
- **Inicio y Fin del Registro**: El sistema de registro marca el inicio y el final del archivo de registro, incluyendo el conteo total de mensajes registrados.
- **Registro de Mensajes**: Los mensajes son registrados en un archivo llamado `log.txt`, cada uno en una nueva línea.
- **Conteo de Mensajes**: Mantiene un conteo de cuántos mensajes han sido registrados.

## Estructura del Código
- La **clase `Logger`** gestiona la apertura, el registro de mensajes y el cierre del archivo de registro. Al ser destruida la instancia de `Logger`, se escribe el mensaje de cierre en el archivo y se cierra el archivo.
- La **clase `Test`** se utiliza para demostrar cómo se puede integrar y utilizar la clase `Logger` para registrar mensajes.

## Uso

### Creación de una Instancia de Logger
Para comenzar a registrar mensajes, primero se crea una instancia de la clase `Logger`:

```python
logger = Logger()

