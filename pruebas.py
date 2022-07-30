''' def mcd(n1, n2):
    if n1 > n2:
        small = n2
    else:
        small = n1

    for i in range(1, small+1):
        if((n1 % i == 0) and (n2 % i == 0)):
            calc_mcd = i
    return calc_mcd '''

''' def exponente(n):
    if n % 2 != 0:
        n = n - 1
        print('n', n)
    
    i = 2
    cont = 0
    while i <= n:
        i = 2 * i
        cont = cont + 1
        print(i)
        print(cont)
    
    return cont '''

''' def panprimo(n):
    cont_panprimo = 0
    cont_primo = 1

    cadena = str(n)

    if '0' in cadena and '1' in cadena and '2' in cadena and '3' in cadena and '4' in cadena and '5' in cadena and '6' in cadena and '7' in cadena and '8' in cadena and '9' in cadena:
        cont_panprimo = 1

    num = n % 1000
    for aux in range(2, num):
        if num % aux == 0:
            cont_primo = 0
    
    if cont_panprimo == 1 and cont_primo == 1:
        return True
    else:
        return False '''

''' print(panprimo(10123485769)) '''

''' def mcd(n1, n2):
    if n1 > n2:
        small = n2
    else:
        small = n1

    for i in range(1, small+1):
        if((n1 % i == 0) and (n2 % i == 0)):
            calc_mcd = i
    return calc_mcd '''

''' def exponente(n):
    if n % 2 != 0:
        n = n - 1
        print('n', n)
    
    i = 2
    cont = 0
    while i <= n:
        i = 2 * i
        cont = cont + 1
        print(i)
        print(cont)
    
    return cont '''

''' def panprimo(n):
    cont_panprimo = 0
    cont_primo = 1

    cadena = str(n)

    if '0' in cadena and '1' in cadena and '2' in cadena and '3' in cadena and '4' in cadena and '5' in cadena and '6' in cadena and '7' in cadena and '8' in cadena and '9' in cadena:
        cont_panprimo = 1

    num = n % 1000
    for aux in range(2, num):
        if num % aux == 0:
            cont_primo = 0
    
    if cont_panprimo == 1 and cont_primo == 1:
        return True
    else:
        return False '''

''' print(panprimo(10123485769)) '''

''' def mezclador(string_a, string_b):
    if len(string_a) > 2 and len(string_b):
        string_a_1 = string_a[0:2]
        string_b_2 = string_b[-2:]
        string_c = string_a_1 + string_b_2
    return string_c

print(mezclador('Carlos', 'Oscar')) '''

''' def intercalar(string_a,string_b):
    r = ""
    i= 0
    l=len(string_a)

    while i < l:
        r = r + string_a[i] + string_b
        i += 1
    return r

print(intercalar('CARLOS', 'oscar')) '''

''' def ocurrencias(string):
    c1 = string.count('1')
    c0 = string.count('0')
    return(c1 - c0)

print(ocurrencias('11001100110')) '''

''' def remover_enesimo(s, n):
    s = list(s)
    if n >= len(s) or n < 0:
        s = "".join(s)
        return s
    else:
        del s[n]
        s = "".join(s)
        return s

print(remover_enesimo('Metodos', 7)) '''

''' def reemplazo(string):
    indice = 0

    while indice < len(string):
        letra = string[indice]
        if letra.isupper() == True:
            string = string.replace(letra, '$')
        indice += 1

    return string

print(reemplazo('Esta Es unA pruebA')) '''

lista = [1, 22, 79, 64, 84, 7, 1, 39, 41, 19, 69]

def promedio_std(lista):
    x = 0
    y = 0
    x = sum(lista) / len(lista)
    total = 0.0
    for i in lista:
        total += round((i - x) ** 2,3)
    y = total / (len(lista))
    y= round(y**(1/2),3)
    return x,y

print(promedio_std(lista))

''' lista = ["azul","rojo","verde","verde","verde","rojo","verde","verde","azul","amarillo","azul","azul","verde","verde","verde","amarillo","amarillo"]

def  color_frecuente(lista):
    lista2 = ["azul", "rojo", "verde", "amarillo"]
    nueva_lista = []
    for i in lista2:
        cantidad = 0
        for j in lista:
            if i == j:
               cantidad = cantidad + 1
        nueva_lista.append([cantidad, i])

    az = nueva_lista.pop(0)
    rj = nueva_lista.pop(0)
    vr = nueva_lista.pop(0)
    am = nueva_lista.pop(0)

    if ((az[0]>=rj[0])and(az[0]>=vr[0])and(az[0]>=am[0])):
        return (az[1],az[0])
    elif ((rj[0]>az[0])and(rj[0]>=vr[0])and(rj[0]>=am[0])):
        return (rj[1],rj[0])
    elif ((vr[0]>az[0]) and (vr[0]>rj[0]) and (vr[0]>=am[0])):
        return (vr[1], vr[0])
    elif ((am[0]>az[0])and(am[0]>rj[0])and(am[0]>vr[0])):
        return (am[1],am[0])

print(color_frecuente(lista)) '''


