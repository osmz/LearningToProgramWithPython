import os
# functions
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

def get_Country():
    country = input("Dinos de que pais eres: ")
    return country

def get_Num_Friends():
    num_friends = int(input("Cuéntame ¿cuantos amigos tienes?: "))
    return num_friends

def get_Data():
    n = get_Name()
    e = get_Age()
    (em, ec) = get_Stature()
    na = get_Num_Friends()
    return (n, e, em, ec, na)

def show_Profile(name, age, stature_m, stature_cm, num_friends, country):
    print("--------------------------------------------------")
    print("Nombre:   ", name)
    print("Edad:     ", age, "años")
    print("Estatura: ", stature_m, "m o ", stature_cm, "centímetros")
    print("Amigos:   ", num_friends)
    print("Pais:     ", country)
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

def file_exists(ruta):
    return os.path.isfile(ruta)

def read_Username(name):
    archivo_usuario = open(name+".user","r")
    name = archivo_usuario.readline()
    age = int(archivo_usuario.readline())
    stature = float(archivo_usuario.readline())
    stature_m = float(stature)
    stature_cm = int(stature_m*100)
    country = archivo_usuario.readline()
    num_friends = int(archivo_usuario.readline())
    message = archivo_usuario.readline()
    # Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return(name, age, stature_m, stature_cm, country, num_friends, message)

def write_Username(name, age, stature_m, country, num_friends, message):
    archivo_usuario = open(name+".user","w")
    archivo_usuario.write(name+"\n")
    archivo_usuario.write(str(age)+"\n")
    archivo_usuario.write(str(stature_m)+"\n")
    archivo_usuario.write(country+"\n")
    archivo_usuario.write(str(num_friends)+"\n")
    archivo_usuario.write(message+"\n")
    # Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()