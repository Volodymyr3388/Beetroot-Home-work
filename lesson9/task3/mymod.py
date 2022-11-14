def count_lines(a):
    s = open(a, "r")
    b = s.readlines()
    c = len(b)
    return c

def count_chars(d):
    g = open(d, "r")
    h = g.read()
    i = len(h)
    return i

def test(j):
    k = count_lines(j), count_chars(j)
    return k

