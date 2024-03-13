# Clase Logger para gestionar el registro de mensajes en un archivo
class Logger:
    def __init__(self):
        self.count = 0
        # Abre (o crea si no existe) el archivo log.txt en modo escritura
        self.log_file = open(".\entregaEjerciciosPOO\log.txt", "w")
        self.log_file.write("--Start log--\n")

    # Se llama automáticamente cuando la instancia de Logger es destruida
    def __del__(self):
        self.log_file.write("--End log: {} log(s)--".format(self.count))
        self.log_file.close()

    # Método para registrar un mensaje en el archivo de log
    def log(self, message):
        self.count += 1
        self.log_file.write(message + "\n")

# Clase Test que utiliza la clase Logger para registrar mensajes
class Test:
    def __init__(self):
        self.logger = Logger()

    # Método que recibe un mensaje y lo pasa al método log de Logger para ser registrado
    def llamada(self, mensaje):
        self.logger.log(mensaje)

def main():
    test = Test()
    for i in range(1, 6):
        if i == 1:
            # Registra la primera llamada con un mensaje específico
            test.llamada("Primera llamada")
        else:
            # Registra las llamadas subsiguientes con un mensaje numerado
            test.llamada("{}ª llamada".format(i))

if __name__ == "__main__":
    main()
