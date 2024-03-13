# Apartados A y B (Ejercicio 1)
class Palindromo:
    def __init__(self, cadena):
        self.cadena = cadena

    @classmethod
    def esPalindromo(cls, cadena):
        # Filtrar la cadena para eliminar caracteres no alfanuméricos y convertirla a minúsculas.
        cadena_filtrada = ''.join(c for c in cadena if c.isalnum()).lower()
        # Comparar la cadena filtrada con su inversa.
        return cadena_filtrada == cadena_filtrada[::-1]
    
    def test(self):
        return self.esPalindromo(self.cadena)
    
    def __del__(self):
        print(self.cadena.upper())


def main():
    # Pruebas del método esPalindromo
    print("TESTEO esPalindromo\n")
    print(Palindromo.esPalindromo('radar'))
    print(Palindromo.esPalindromo('sonar'))
    print(Palindromo.esPalindromo('Arde ya la yedra'))
    print(Palindromo.esPalindromo('Ardeyalayedra'))
    print(Palindromo.esPalindromo('!@#$% %$#@!'))
    print(Palindromo.esPalindromo('L O L'))

    # Pruebas del método test y comportamiento al destruir la instancia
    print("\nTESTEO método test:\n")
    p = Palindromo("radar")
    print(p.test())

    # Creación de una nueva instancia para demostrar la impresión al destruir la instancia
    p = Palindromo("sonar")
    print(p.test())

if __name__ == "__main__":
    main()