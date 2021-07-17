def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b)

uscln(20,5)