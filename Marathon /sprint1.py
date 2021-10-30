import collections


def kthTerm(n, k):
    c = []
    power = 0
    while len(c) <= k:
        x = [(n**power + c[i]) for i in range(len(c))]
        c.append(n**power)
        c += x
        power += 1
    return c[k-1]


def filterBible(scripture, book, chapter):
    filtered_b = []
    for i in scripture:
        if i[:2] == book:
            if i[2:5] == chapter:
                filtered_b.append(i)
    return filtered_b


def filterBible_dar(x, q, w):
    return list(filter(lambda n: n[:2] == q and n[2:5] == w, x))


def isPalindrome(str):
    odd_letter = 0
    c = collections.Counter(str)
    for count_letter in c.values():
        if count_letter % 2:
            odd_letter += 1
    return odd_letter <= 1


def findPermutation(n, p, q):
    r = []
    for i in range(n):
        r.append(p.index(q[i])+1)
    return r


def order(a):
    if sorted(a) == a:
        return "ascending"
    elif sorted(a, reverse=True) == a:
        return "descending"
    return "not sorted"


def Cipher_Zeroes(N):
    priz = 0
    for i in str(N):
        if i == "0" or i == "6" or i == "9":
            priz += 1
        elif i == "8":
            priz += 2
    if not priz % 2 and priz != 0:
        return "{0:b}".format(priz - 1)
    if priz % 2 and priz != 0:
        return "{0:b}".format(priz + 1)
    return priz


def studying_hours(a):
    days = 1
    days_list = []
    for i in range(1, len(a)):
        if a[i-1] <= a[i]:
            days += 1
        else:
            days_list.append(days)
            days = 1
    days_list.append(days)
    return max(days_list)


class Stack():
    def __init__(self):
        self.size = 0
        self.content = list()

    def is_empty(self):
        return not bool(self.content)

    def push(self,elem):
        self.content.append(elem)
        self.size = len(self.content)-1

    def pop(self):
        if not self.is_empty():
            elem = self.content.pop()
            size = len(self.content)-1
            return elem
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.content[-1]
        else:
            return None

    def display(self):
        if not self.is_empty():
            return self.content
        else:
            return None


def toPostFixExpression(e):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfixList = []

    for token in e:
        if token.isdigit():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return postfixList
