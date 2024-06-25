def no_space(texto):
    texto_nuevo = ""
    for char in texto:
        if char != " ":
            texto_nuevo += char
    return texto_nuevo


def es_palindromo(texto):
    texto = no_space(texto)
    print(texto)


es_palindromo("amo la paloma")
