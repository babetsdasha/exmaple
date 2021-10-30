import re


def morse_number(s):
    def repl(m):
        n = int(m.group(0))
        if n >= 1 and n <= 5:
            return ("." * n) + "-" * (5 - n) + " "
        elif n > 5 and n <= 9:
            return "-" * (n - 5) + ("." * (5 + (5 - n))) + " "
        else:
            return "-" * 5 + " "
    return re.sub(r"(\d)", repl, s)


def double_string(s):
    b = []
    count = 0
    for i in s:
        for x in s:
            b.append(i+x)
    for i in s:
        if i in b:
            count += 1
    return count


def figure_perimetr(s):
    dots = re.findall(r"\d:\d", s)
    perim = 0
    x, y = [], []
    for i in dots:
        x.append(int(i[:1]))
        y.append(int(i[-1:]))
    perim += ((x[0]-x[1])**2 + (y[0]-y[1])**2)**0.5
    perim += ((x[1]-x[3])**2 + (y[1]-y[3])**2)**0.5
    perim += ((x[3]-x[2])**2 + (y[3]-y[2])**2)**0.5
    perim += ((x[2]-x[0])**2 + (y[2]-y[0])**2)**0.5
    return perim
