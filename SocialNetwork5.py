import funtionSocialNetwork as Red

Red.show_Welcome()
name = Red.get_Name()
print()
print("Hola ", name, ", bienvenido a Mi Red")

# Verificamos si el archivo existe
if Red.file_exists(name+".user"):
    # Esto lo hacemos si ya habíaa un usuario con ese nombre
    print("Leyendo datos de usuario", name, "desde archivo.")
    (name, age, stature_m, stature_cm, country, num_friends, message) = Red.read_Username(name)
else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo hacíamos antes
    print()
    age = Red.get_Age()
    (stature_m, stature_cm) = Red.get_Stature()
    country = Red.get_Country()
    num_friends = Red.get_Num_Friends()
    message = ""

print("Muy bien. Estos son los datos de tu perfil.")
Red.show_Profile(name, age, stature_m, stature_cm, num_friends, country)
Red.show_Message(name, None, message)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con Mi Red. ")
print("--------------------------------------------------")

# Ingresamos al ciclo que permite ejecutar acciones
option = 1
while option != 0:
    # Mostramos el menu
    option = Red.option_Menu()

    # Código para la opción 1. Publicar un mensaje.
    if option == 1:
        message = Red.get_Message()
        Red.show_Message(name, None, message)

    # Código para la opción 2. Publicar un mensaje a un grupo de personas.
    elif option == 2:
        message = Red.get_Message()
        for i in range(num_friends):
            name_friends = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.show_Message(name, name_friends, message)

    # Código para la opción 3. Publicar los datos del perfil del usuario.
    elif option == 3:
        Red.show_Profile(name, age, stature_m, stature_cm, num_friends, country)

    # Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif option == 4:
        print()
        name = Red.get_Name()
        print()
        age = Red.get_Age()
        print()
        (stature_m, stature_cm) = Red.get_Stature()
        print()
        num_friends = Red.get_Num_Friends()
        print()
        country = Red.get_Country()
        print()
        Red.show_Profile(name, age, stature_m, stature_cm, num_friends, country)
    
     # Código para la opción 0. salir del sistema.
    elif option == 0:
        print("Has decidido salir.\nGuardando perfil en ",name+".user")
        Red.write_Username(name, age, stature_m, country, num_friends, message)
        print("Archivo",name+".user","guardado")

print("Gracias por usar Mi Red. ¡Hasta pronto!")