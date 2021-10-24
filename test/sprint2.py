from posixpath import split
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
    # b = x.pop()
    # c = x.pop()
    # x.append(b)
    # x.append(c)
    # b = y.pop()
    # c = y.pop()
    # y.append(b)
    # y.append(c)
    # for i in range(4):
    #     perim += ((x[i]-x[i])**2 + (y[i]-y[i])**2)**0.5
    perim += ((x[0]-x[1])**2 + (y[0]-y[1])**2)**0.5
    perim += ((x[1]-x[3])**2 + (y[1]-y[3])**2)**0.5
    perim += ((x[3]-x[2])**2 + (y[3]-y[2])**2)**0.5
    perim += ((x[2]-x[0])**2 + (y[2]-y[0])**2)**0.5
    return perim


test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))

test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))


# import re


# def max_population(l):
#     name = []
#     poppulation = []
#     for i in l:
#         b = i.split(",")
#         name.append(b[1])
#         poppulation.append(b[2])
#     poppulation[0] = 0
#     x = poppulation.index(max(poppulation))
#     print(poppulation)
#     return (name[x], poppulation[x])

# data = ["id,name,poppulation,is_capital",
# "3024,eu_kyiv,24834,y",
# "3025,eu_volynia,20231,n",
# "3026,eu_galych,23745,n",
# "4892,me_medina,18038,n",
# "4401,af_cairo,18946,y",
# "4700,me_tabriz,13421,n",
# "4899,me_bagdad,22723,y",
# "6600,af_zulu,09720,n"]

# print(max_population(data))


# import re


# def pretty_message(text):
#     p1 = re.compile(r"(\w)\1+")
#     p2 = re.compile(r"(\w{2,3})\1+")
#     text = re.sub(p1, r"\1", text)
#     text = re.sub(p2, r"\1", text)
#     return text


# data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
# print(pretty_message(data))


# import re


# def max_population(data):
#     splited = [re.split(",", i) for i in data[1:]]
#     print(splited)
#     m = max(splited, key=lambda x: int(x[2]))
#     return m[1], int(m[2])

# data = ["id,name,poppulation,is_capital",
# "3024,eu_kyiv,24834,y",
# "3025,eu_volynia,20231,n",
# "3026,eu_galych,23745,n",
# "4892,me_medina,18038,n",
# "4401,af_cairo,18946,y",
# "4700,me_tabriz,13421,n",
# "4899,me_bagdad,22723,y",
# "6600,af_zulu,09720,n"]

# print(max_population(data))

# import re


# def pretty_message(text):
#     p1 = re.compile(r"(\w)\1+")
#     p2 = re.compile(r"(\w{2,3})\1+")
#     text = re.sub(p1, r"\1", text)
#     text = re.sub(p2, r"\1", text)
#     return text
