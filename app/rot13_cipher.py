import string


def cif_rot(str_in, shift):
    ap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(str_in)
    str_out = ""

    for i in range(n):
        c = str_in[i].upper()
        l = ap.find(c)
        newloc = (l + shift) % 26
        str_out += ap[newloc]

    return str_out


def cif_rot13(msg):
    return cif_rot(msg, 13)


def cif_cesar(msg):
    return cif_rot(msg, 3)


print(cif_cesar("foobar"))
print(cif_rot("foobar"))


def cif_rot_2(n):
    lw = string.ascii_lowercase
    up = string.ascii_uppercase
    tr = str.maketrans(lw + up, lw[:n] + up[:n])
    return lambda s: str.translate(s, tr)


def cif_cesar_2():
    return cif_rot_2(3)


def cif_rot13_2():
    return cif_rot_2(13)


cesar = cif_cesar_2()
rot13 = cif_rot13_2()

print(cesar("footbar"))
print(rot13("footbar"))
