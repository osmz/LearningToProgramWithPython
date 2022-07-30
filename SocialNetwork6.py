import funtionSocialNetwork6 as Red

Red.show_welcome()
name = Red.get_Name()
print("Hola ", name, ", bienvenido a Mi Red")

#Verificamos si el archivo existe
if Red.existe_archivo(name+".user"):
    #Esto lo hacemos si ya habÃ­a un usuario con ese name
    print("Leyendo datos de usuario", name, "desde archivo.")
    (name, age, stature_m, stature_cm, sexo, country, friends, message, muro) = Red.read_Username(name)

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo hacÃ­amos antes
    print()
    age = Red.get_Age()
    (stature_m, stature_cm) = Red.get_Stature()
    sexo = Red.get_Sexo()
    country = Red.get_Country()
    friends = Red.get_List_Friends()
    message = ""
    muro = []

#En ambos casos, al llegar aquÃ­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.show_Profile(name, age, stature_m, stature_cm, sexo, country, friends)
Red.show_Message(name, message)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.option_Menu()
    if opcion == 1:
        message = Red.get_Message()
        Red.post_Message(name, friends, message, muro)
    elif opcion == 2:
        Red.show_Muro(muro)
    elif opcion == 3:
        Red.show_Profile(name, age, stature_m, stature_cm, sexo, country, friends)
    elif opcion == 4:
        age = Red.get_Age()
        (stature_m, stature_cm) = Red.get_Stature()
        sexo = Red.obtener_sexo()
        country = Red.get_Country()
        friends = Red.get_List_Friends()
        Red.show_Profile(name, age, stature_m, stature_cm, sexo, country, friends)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",name+".user")
        Red.write_Username(name, age, stature_m, stature_cm, sexo, country, friends, message,muro)
        print("Archivo",name+".user","guardado")

print("Gracias por usar Mi Red. ¡Hasta pronto!")