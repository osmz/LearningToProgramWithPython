# Funciones

# Mensaje de bienvenida al usuario
def show_Welcome():
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

def get_Name():
    name = input("Dinos como te llamas: ")
    return name

def get_Age():
    year = int(input("Para preparar tu perfil, dime en que año naciste. "))
    return 2022-year

def get_Stature():
    stature = float(input("¿Cuánto mides en metros?: "))
    stature_m = float(stature)
    stature_cm = int(stature_m*100 )
    return (stature_m, stature_cm)

def get_Num_Friends():
    num_friends = int(input("Cuéntame ¿cuantos amigos tienes?: "))
    return num_friends

def show_Profile(name, age, stature_m, stature_cm, num_friends):
    print("--------------------------------------------------")
    print("Nombre:   ", name)
    print("Edad:     ", age, "años")
    print("Estatura: ", stature_m, "m o ", stature_cm, "centímetros")
    print("Amigos:   ", num_friends)
    print("--------------------------------------------------")

def option_Menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    option = int(input("Ingresa una opción: "))
    while option < 0 or option > 4:
        print("No conozco la opción que has ingresado. Inténtalo otra vez: ")
        option = int(input("Ingresa una opción: "))
    return option

def get_Message():
    message = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy?: ")
    return message

def show_Message(origin, addressee, message):
    print("--------------------------------------------------")
    if addressee == None:
        print(origin, "dice:", message)
    else:
        print(origin, "dice:", "@"+addressee, message)
    print("--------------------------------------------------")

show_Welcome()
name = get_Name()
print()
print("Hola ", name, ", bienvenido a Mi Red")
print()
age = get_Age()
print()
(stature_m, stature_cm) = get_Stature()
print()
num_friends = get_Num_Friends()
print()
print("Muy bien,", name, ". Entonces podemos crear un perfil con estos datos: ")
show_Profile(name, age, stature_m, stature_cm, num_friends)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con Mi Red. ")
print("--------------------------------------------------")

# Ingresamos al ciclo que permite ejecutar acciones
option = 1
while option != 0:
    # Mostramos el menu
    option = option_Menu()

    # Código para la opción 1. Publicar un mensaje.
    if option == 1:
        message = get_Message()
        show_Message(name, None, message)

    # Código para la opción 2. Publicar un mensaje a un grupo de personas.
    elif option == 2:
        message = get_Message()
        for i in range(num_friends):
            name_friends = input("Ingresa el nombre de tu amigo o amiga: ")
            show_Message(name, name_friends, message)

    # Código para la opción 3. Publicar los datos del perfil del usuario.
    elif option == 3:
        show_Profile(name, age, stature_m, stature_cm, num_friends)

    # Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif option == 4:
        print()
        name = get_Name()
        print()
        age = get_Age()
        print()
        (stature_m, stature_cm) = get_Stature()
        print()
        num_friends = get_Num_Friends()
        print()
        show_Profile(name, age, stature_m, stature_cm, num_friends)
    elif option == 0:
        print("Has decidido salir.")

print("Gracias por usar Mi Red. ¡Hasta pronto!")