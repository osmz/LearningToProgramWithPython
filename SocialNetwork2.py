# Funciones

def postMessage(name, message):
    print()
    print("--------------------------------------------------")
    print(name, "dice:", message)
    print("--------------------------------------------------")

# Mensaje de bienvenida al usuario
print("Bienvenido a Mi red social... ")
print("""
  ____ ____  ____ ____ ____ ____ 
 / ___) _  |/ ___) _  ) ___) _  |
( (__( ( | | |  ( (/ ( (__( ( | |
 \____)_||_|_|   \____)____)_||_|
                                   _          
             _                    | |         
 ____   ____| |_ _ _ _  ___   ____| |  _  ___ 
|  _ \ / _  )  _) | | |/ _ \ / ___) | / )/___)
| | | ( (/ /| |_| | | | |_| | |   | |< (|___ |
|_| |_|\____)\___)____|\___/|_|   |_| \_|___/

""")

# Solicitamos al usuario que ingrese su nombre, y lo guardamos en una variable de tipo str
name = input("Dinos como te llamas: ")
print()
print("Hola ", name, ", bienvenido a Careca Networks.")
print()

# Solicitamos el ingreso del año, y utilizamos este dato para estimar la edad de la persona. 
year = int(input("Para preparar tu perfil, dime en que año naciste. "))
age = 2022-year
print()

# Solicitamos la estatura, medida en metros. Utilizamos la conversión a 'int', y una expresión para convertir esto a una medida en metros y centí­metros
print("Queremos saber mas de ti, vamos a realizarte algunas preguntas.")
print()
stature = float(input("¿Cuánto mides en metros?: "))
stature_m = float(stature)
stature_cm = int(stature_m*100 )
print()

# Consultamos el género del usuario.
gender = input("¿Cuál es tu género?: ")
print()

# Consultamos el número de contacto.
number = str(input("¿Ingresa tu número de contacto?: "))
print()

# Consultamos la ciudad en donde vive el usuario.
city = str(input("¿En qué ciudad vives?: "))
print()

# Consultamos cuántos amigos tiene el usuario.
num_friends = int(input("Muy bien. Finalmente, cuéntame ¿cuantos amigos tienes?. "))
print()

# Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", name, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", name)
print("Edad:    ", age, "años")
print("Estatura:", stature_m, "metros o", stature_cm, "centímetros")
print("Género:  ", gender)
print("Número de contacto:  ", number)
print("Ciudad:  ", city)
print("Amigos:  ", num_friends)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes de nuestra red.")
print()

# Solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
message = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
postMessage(name, message)

''' # Usaremos una variable bool para indicar si el usuario desea continuar utilizando el programa o no
continuar = True

# Este ciclo se mantiene en ejecuciónn hasta que el usuario desee salir
while continuar:

    # Solicitamos opción al usuario
    escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N) "))

    # Si el usuario ingrese "N" o "n", termina el programa
    if escribir_mensaje == "N" or escribir_mensaje == "n":
        continuar = False
    # En caso que sea otra respuesta, vamos a publicar otro mensaje
    else:
        menssage = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(name, "dice:", menssage)
        print("--------------------------------------------------")

# Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Careca networks. ¡Hasta pronto!") '''

# Esta opcion permite entrar al ciclo. Solo interesa que no sea 0.
option = 1
while option != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    option = int(input("Ingresa una opción: "))

    # Código para la opción 1. Publicar un mensaje.
    if option == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        postMessage(name, message)

    # Código para la opción 2. Publicar un mensajes a un grupo de personas.
    elif option == 2:
        message = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
        print()
        for i in range(num_friends):
            name_friends = input("Ingresa el nombre de tu amigo o amiga: ")
            print("--------------------------------------------------")
            print(name, "dice:", "@"+name_friends, message)
            print("--------------------------------------------------")

    # Código para la opción 3. Publicar los datos del perfil del usuario.
    elif option == 3:
        print("--------------------------------------------------")
        print("Nombre:   ", name)
        print("Edad:     ", age, "años")
        print("Estatura: ", stature_m, "m o ", stature_cm, "centímetros")
        print("Amigos:   ", num_friends)
        print("--------------------------------------------------")

    # Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif option == 4:
        # Repetimos el código para solicitar datos
        # Solicitud de nombre
        name = input("Para empezar, dime como te llamas. ")
        print()
        print("Hola ", name, ", bienvenido a Mi Red")
        print()

        # Cálculo de edad
        year = int(input("Para preparar tu perfil, dime en que año naciste. "))
        age = 2022-year
        print()

        # Cálculo de estatura
        print("Queremos saber mas de ti, vamos a realizarte algunas preguntas.")
        print()
        stature = float(input("¿Cuánto mides en metros?: "))
        stature_m = float(stature)
        stature_cm = int(stature_m*100 )
        print()

        # Cantidad de amigos
        num_friends = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

        print()
        print("Muy bien,", name, ". Entonces podemos crear un perfil con estos datos.")
        # Repetimos el código para mostrar los datos del usuario.
        print("--------------------------------------------------")
        print("Nombre:  ", name)
        print("Edad:    ", age, "años")
        print("Estatura:", stature_m, "metros y", stature_cm, "centímetros")
        print("Amigos:  ", num_friends)
        print("--------------------------------------------------")
        print()

    # Código para la opción 0. Salir.
    elif option == 0:
        print("Has decidido salir.")

    # Código para la opción que no coincida con ninguna anterior.
    else:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")

print()
print("Gracias por usar Mi red Careca Networks. ¡Hasta pronto!")
print()

