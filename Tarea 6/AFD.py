# PARSER, ARCHIVOS .AON

# TOKEN

tk_parA = "("
tk_parB = ")"
tk_menorQ = "<"
tk_mayorQ = ">"
tk_corchA = "["
tk_corchB = "]"
tk_igual = "="
tk_coma = ","
tk_comilla = """ "' """

tk_palabra = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyzáéíóúàèìòùäëïöü|¡!#$%&/¿?.,;-_"""
tk_numero = "1234567890-."

# TEXTO

texto = """(
<
    [atributo_numerico] = 45.09,
    [atributo_cadena] = "hola mundo",
    [atributo_booleano] = true
>,
<
    [atributo_numerico] = 4,
    [atributo_cadena] = "adios mundo",
    [atributo_booleano] = false
>,
<
    [atributo_numerico] = -56.4,
    [atributo_cadena] = "este es otro ejemplo, las cadenas pueden ser muy largas",
    [atributo_booleano] = false
>
)"""


# AUTÓMATA FINITO

def AFD(texto):
    estado = 0
    palabra = ""
    tokens = []

    try:
        for char in texto:

            if char != " " and char != "\n":
                if estado == 0:
                    if char == tk_parA:
                        estado = 1
                        tokens.append([char, "TOKEN: tk_parA"])
                    else:
                        err += 1

                elif estado == 1:
                    if char == tk_menorQ:
                        estado = 2
                        tokens.append([char, "TOKEN: tk_menorQ"])
                    else:
                        err += 1

                elif estado == 2:
                    if char == tk_corchA:
                        estado = 3
                        tokens.append([char, "TOKEN: tk_corchA"])
                    else:
                        err += 1

                elif estado == 3:
                    if char in tk_palabra:
                        estado = 4
                        palabra = palabra+char
                    else:
                        err += 1

                elif estado == 4:
                    if char in tk_palabra:
                        estado = 4
                        palabra = palabra+char

                    elif char == tk_corchB:
                        tokens.append([palabra, "TOKEN: tk_palabra"])
                        palabra = ""

                        estado = 5
                        tokens.append([char, "TOKEN: tk_corchB"])
                    else:
                        err += 1

                elif estado == 5:
                    if char == tk_igual:
                        estado = 6
                        tokens.append([char, "TOKEN: tk_igual"])
                    else:
                        err += 1

                elif estado == 6:
                    if char in tk_numero:
                        estado = 7
                        palabra = palabra+char
                    elif char in tk_comilla:
                        estado = 8
                        tokens.append([char, "TOKEN: tk_comilla"])
                    elif char in tk_palabra:
                        estado = 11
                        palabra = palabra+char
                    else:
                        err += 1

                elif estado == 7:
                    if char in tk_numero:
                        estado = 7
                        palabra = palabra+char

                    elif char == tk_coma:
                        tokens.append([palabra, "TOKEN: tk_palabra"])
                        palabra = ""

                        estado = 10
                        tokens.append([char, "TOKEN: tk_coma"])
                    elif char == tk_mayorQ:
                        tokens.append([palabra, "TOKEN: tk_integer"])
                        palabra = ""

                        estado = 12
                        tokens.append([char, "TOKEN: tk_mayorQ"])
                    else:
                        err += 1

                elif estado == 8:
                    if char in tk_palabra:
                        estado = 8
                        palabra = palabra+char

                    elif char in tk_comilla:
                        tokens.append([palabra, "TOKEN: tk_palabra"])
                        palabra = ""

                        estado = 9
                        tokens.append([char, "TOKEN: tk_comilla"])
                    else:
                        err += 1

                elif estado == 9:
                    if char == tk_coma:
                        estado = 10
                        tokens.append([char, "TOKEN: tk_coma"])
                    elif char == tk_mayorQ:
                        estado = 12
                        tokens.append([char, "TOKEN: tk_mayor!"])
                    else:
                        err += 1

                elif estado == 10:
                    if char == tk_corchA:
                        estado = 3
                        tokens.append([char, "TOKEN: tk_corchA"])
                    else:
                        err += 1

                elif estado == 11:
                    if char in tk_palabra:
                        estado = 11
                        palabra = palabra+char

                    elif char == tk_coma:
                        if palabra.lower() != "true" and palabra.lower() != "false":
                            print("'"+palabra+"' no es un atributo boolean")
                            err += 1
                        else:
                            tokens.append([palabra, "TOKEN: tk_boolean"])

                        palabra = ""

                        estado = 10
                        tokens.append([char, "TOKEN: tk_coma"])
                    elif char == tk_mayorQ:
                        if palabra.lower() != "true" and palabra.lower() != "false":
                            print("'"+palabra+"' no es un atributo boolean")
                            err += 1
                        else:
                            tokens.append([palabra, "TOKEN: tk_boolean"])

                        palabra = ""

                        estado = 12
                        tokens.append([char, "TOKEN: tk_mayorQ"])
                    else:
                        err += 1

                elif estado == 12:
                    if char == tk_coma:
                        estado = 1
                        tokens.append([char, "TOKEN: tk_coma"])
                    elif char == tk_parB:
                        estado = 13
                        tokens.append([char, "TOKEN: tk_parB"])
                    else:
                        err += 1

                elif estado == 13:
                    print("LA CADENA ES VÁLIDA")

        print("LEXEMA    TOKEN\n")
        for par in tokens:
            print(par)

    except:
        print("""
La cadena:

    """+texto+"""

es INVALIDA""")
        print("")


# EJECUCIÓN

AFD(texto)
