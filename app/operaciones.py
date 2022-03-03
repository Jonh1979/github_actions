def suma(x, y):
    """Función que recibe dos parámetros y devuelve la suma de los dos.

    >>> suma(10, 5)
    15
    """
    return x + y


def resta(x, y):
    """Función que recibe dos parámetros y devuelve la resta de los dos.

    >>> resta(10, 5)
    5
    """
    return x - y


def multiplicacion(x, y):
    """Función que recibe dos parámetros y devuelve la multiplicación de los dos.

    >>> multiplicacion(10, 5)
    50
    """
    return x * y


def division(x, y):
    """Función que recibe dos parámetros y devuelve la división real de los dos.

    >>> division(10, 5)
    2.0
    """
    return x / y


def cociente(x, y):
    """Función que recibe dos parámetros y devuelve el cociente de la división entera de los dos.

    >>> cociente(11, 5)
    2
    """
    return x // y


def resto(x, y):
    """Función que recibe dos parámetros y devuelve el resto de la división entera de los dos.

    >>> resto(11, 5)
    1
    """
    return x % y

def rot13_cipher(str_in, shift):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(str_in)
    str_out = ""

    for i in range(n):
        c = str_in[i].upper()
        loc = alpha.find(c)
        newloc = (loc + shift) % 26
        str_out += alpha[newloc]

    return str_out


def rot13_cipher2(msg):
    return rot13_cipher(msg, 13)


def cifrado_cesar(msg):
    return rot13_cipher(msg, 3)


print(cifrado_cesar("foobar"))
print(rot13_cipher("foobar"))


def cifrado_rot_2(n):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = str.maketrans(lc + uc, lc[:n] + lc[:n] + uc[:n] + uc[:n])
    return lambda s: str.translate(s, trans)


def cifrado_cesar_2():
    return cifrado_rot_2(3)


def rot13_cipher_2():
    return cifrado_rot_2(13)


cesar = cifrado_cesar_2()
rot13 = rot13_cipher_2()

print(cesar("footbar"))
print(rot13("footbar"))
