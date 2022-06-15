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
print("Hola ", name, ", bienvenido a Careca Networks")
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
gender = int(input("¿Cuál es tu género?: "))
print()

# Consultamos el número de contacto.
number = int(input("¿Ingresa tu número de contacto?: "))
print()

# Consultamos la ciudad en donde vive el usuario.
city = int(input("¿En qué ciudad vives?: "))
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
print("Gracias por la información. Esperamos que disfrutes de nuestra red")
print()

# Solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
message = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
print()
print("--------------------------------------------------")
print(name, "dice:", message)
print("--------------------------------------------------")