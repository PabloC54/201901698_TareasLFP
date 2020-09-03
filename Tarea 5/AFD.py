# INICIALIZANDO

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
guion = '_'

cadena1 = '__servidor1'
cadena2 = '3servidor'


# AUTÓMATA FINITO

def AFD(texto):
    estado, i = 0, 1

    try:
        for char in texto:
            print("=> "+char)

            if estado == 0:
                if char in letras:
                    estado = 2
                elif char == guion:
                    estado = 1
                else:
                    err += 1

            elif estado == 1:
                if char in letras:
                    estado = 3
                elif char == guion:
                    estado = 1
                else:
                    err += 1

            elif estado == 2:
                if char in letras:
                    estado = 2
                elif char in numeros:
                    estado = 4
                else:
                    err += 1

            elif estado == 3:
                if char in numeros:
                    estado = 4
                else:
                    err += 1

            if estado == 4:
                if i == len(texto):
                    print("La cadena '"+texto+"' es VALIDA")
                else:
                    err += 1

            i += 1

    except:
        print("La cadena '"+texto+"' es INVALIDA")
        print("")


# EJECUCIÓN
AFD(cadena1)
print("")
AFD(cadena2)
