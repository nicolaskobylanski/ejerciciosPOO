class A:
    # Método que devuelve la instancia actual
    def z(self):
        return self
    
    # Método que recibe un iterable 't' y devuelve su longitud
    def y(self, t):
        return len(t)


def main():
    # Creamos una instancia de A y llamamos a z sobre esa instancia
    a = A()
    y = a.z()

    # Imprime la instancia de la clase A
    print(y)

    # Comprueba si dos instancias distintas de la clase A son la misma (esto siempre será Falso)
    print(a is A())

    # Llama al método y de la instancia 'aa', pasando una tupla vacía como argumento. Esto devolverá 0.
    z = a.y
    print(z(()))

    # Llama directamente al método y sobre una nueva instancia de A, pasando una tupla con un elemento
    print(A().y((A,)))

    # Se llama al método y de la instancia 'aa', pasando una tupla con dos elementos: la clase A y el método z
    print(A.y(a, (A,z)))

    # Llama al método y de la instancia 'aa', pasando una tupla con tres elementos: el método z, el número 1, y el string 'z'
    print(a.y((z,1,'z')))

if __name__ == "__main__":
    main()
