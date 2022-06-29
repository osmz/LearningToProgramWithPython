import funtionSocialNetwork as Red

Red.show_Welcome()
name = Red.get_Name()
print()
print("Hola ", name, ", bienvenido a Mi Red")
print()
age = Red.get_Age()
print()
(stature_m, stature_cm) = Red.get_Stature()
print()
num_friends = Red.get_Num_Friends()
print()
print("Muy bien,", name, ". Entonces podemos crear un perfil con estos datos: ")
Red.show_Profile(name, age, stature_m, stature_cm, num_friends)
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
        Red.show_Profile(name, age, stature_m, stature_cm, num_friends)

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
        Red.show_Profile(name, age, stature_m, stature_cm, num_friends)
    elif option == 0:
        print("Has decidido salir.")

print("Gracias por usar Mi Red. ¡Hasta pronto!")