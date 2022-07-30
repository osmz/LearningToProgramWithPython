import os
# functions
def show_welcome():
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

def get_Sexo():
    sexo = input("Por favor, ingresa tu sexo (M = Masculino, F = Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    return sexo

def get_Country():
    country = input("Dinos de que pais eres: ")
    return country

def get_List_Friends():
    linea = input("Muy bien. Finalmente, escribe una lista con los nombres de tus amigos, separados por una ',': ")
    friends= linea.split(",")
    return friends

def show_Profile(name, age, stature_m, stature_cm, sexo, country, friends):
    print("--------------------------------------------------")
    print("Nombre:   ", name)
    print("Edad:     ", age, "años")
    print("Estatura: ", stature_m, "m o ", stature_cm, "centímetros")
    print("Sexo:     ", sexo) 
    print("Pais:     ", country)  
    print("Amigos:   ", len(friends), "que son: ", friends, )
    print("--------------------------------------------------")

def option_Menu():
    print("Acciones disponibles:")
    print("  1. Escribir un message público")
    print("  2. Escribir un message solo a algunos amigos")
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

def show_Message(origen, message):
    print("--------------------------------------------------")
    print(origen+":", message)
    print("--------------------------------------------------")

# Muestra los mensajes recibidos
def show_Muro(muro):
     print("------ MURO ("+str(len(muro))+" mensaje) ---------")
     for message in muro:
         print(message)
     print("--------------------------------------------------")

#Publica un message en el timeline personal y en el de los amigos
def post_Message(origen, friends, message, muro):
    print("--------------------------------------------------")
    print(origen, "dice:", message)
    print("--------------------------------------------------")
    #Agrega el message al final del timeline local
    muro.append(message)
    #Agrega, al final del archivo de cada amigo, el message publicado
    for friends in friends:
        if existe_archivo(friends+".user"):
            archivo = open(friends+".user","a")
            archivo.write(origen+":"+message+"\n")
            archivo.close()

def existe_archivo(ruta):
    return os.path.isfile(ruta)

def read_Username(name):
    archivo_usuario = open(name+".user","r")
    name = archivo_usuario.readline().rstrip()
    age = int(archivo_usuario.readline())
    stature = float(archivo_usuario.readline())
    stature_m = float(stature)
    stature_cm = int(stature_m*100)
    sexo = archivo_usuario.readline().rstrip()
    country = archivo_usuario.readline().rstrip()
    friends= archivo_usuario.readline().rstrip().split(",")
    message = archivo_usuario.readline().rstrip()
    #Lee el 'muro'. Esto es, todos los messages que han sido publicados en el timeline del usuario.
    muro = []
    message = archivo_usuario.readline().rstrip()
    while message != "":
        muro.append(message)
        message = archivo_usuario.readline().rstrip()
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return(name, age, stature_m, stature_cm, sexo, country, friends, message, muro)

def write_Username(name, age, stature_m, stature_cm, sexo, country, friends, message, muro):
    archivo_usuario = open(name+".user","w")
    archivo_usuario.write(name+"\n")
    archivo_usuario.write(str(age)+"\n")
    archivo_usuario.write(str(stature_m + stature_cm)+"\n")
    archivo_usuario.write(str(sexo)+"\n")
    archivo_usuario.write(country+"\n")
    archivo_usuario.write(",".join(friends)+"\n")
    # Escribe el 'timeline' en el archivo, a continuaciónn del último estado
    for message in muro:
        archivo_usuario.write(message+"\n")
    #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()