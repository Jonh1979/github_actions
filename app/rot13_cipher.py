import string


def cifrado_rot(str_in, shift):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(str_in)
    str_out = ""

    for i in range(n):
        c = str_in[i].upper()
        loc = alpha.find(c)
        newloc = (loc + shift) % 26
        str_out += alpha[newloc]

    return str_out


def cifrado_rot13(msg):
    return cifrado_rot(msg, 13)


def cifrado_cesar(msg):
    return cifrado_rot(msg, 3)


print(cifrado_cesar("foobar"))
print(cifrado_rot13("foobar"))


def cifrado_rot_2(n):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = str.maketrans(lc + uc, lc[:n] + uc[:n] + uc[:n])
    return lambda s: str.translate(s, trans)


def cifrado_cesar_2():
    return cifrado_rot_2(3)


def cifrado_rot13_2():
    return cifrado_rot_2(13)


cesar = cifrado_cesar_2()
rot13 = cifrado_rot13_2()

print(cesar("footbar"))
print(rot13("footbar"))
