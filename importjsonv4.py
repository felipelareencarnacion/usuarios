import json

# Datos iniciales
datos_iniciales = [
    {"nombre": "Usuario1", "edad": 25, "email": "usuario1@example.com"},
    {"nombre": "Usuario2", "edad": 30, "email": "usuario2@example.com"},
    {"nombre": "Usuario3", "edad": 28, "email": "usuario3@example.com"}
]

# Nombre del archivo donde se guardarán los datos
archivo_datos = 'datos.json'

# Función para cargar datos desde el archivo JSON
def cargar_datos_desde_archivo():
    try:
        with open(archivo_datos, 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = datos_iniciales  # Si el archivo no existe, empezamos con los datos iniciales
    return datos

# Función para guardar datos en el archivo JSON
def guardar_datos_en_archivo(datos):
    with open(archivo_datos, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Función para agregar un nuevo usuario
def agregar_usuario(nombre, edad, email):
    datos = cargar_datos_desde_archivo()
    nuevo_usuario = {"nombre": nombre, "edad": edad, "email": email}
    datos.append(nuevo_usuario)
    guardar_datos_en_archivo(datos)

# Función para listar todos los usuarios
def listar_usuarios():
    datos = cargar_datos_desde_archivo()
    for usuario in datos:
        print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Email: {usuario['email']}")

def main():
    while True:
        print("\nBienvenido a la aplicación de gestión de usuarios:")
        print("1. Mostrar usuarios")
        print("2. Agregar usuario")
        print("3. Salir")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            listar_usuarios()
        elif opcion == '2':
            nombre = input("Ingrese el nombre del usuario: ")
            edad = int(input("Ingrese la edad del usuario: "))
            email = input("Ingrese el email del usuario: ")
            agregar_usuario(nombre, edad, email)
            print("Usuario agregado exitosamente.")
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
