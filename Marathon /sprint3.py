import random
from collections import Counter


def outer(name):
    def inner():
        print("Hello, " + name + "!")
    return inner


def divisor(num):
    for i in range(1, num+1):
        if not num % i:
            yield i
    while True:
        yield


def logger(func_first=False):
    def inner(funk):
        def wrapper(*args, **kwargs):
            total = list(args) + list(kwargs.values())
            text = f"Executing of function {funk.__name__} with arguments {', '.join(map(str, total))}..."
            if func_first:
                resp = funk(*args, **kwargs)
                print(text)
                return resp
            else:
                print(text)
                return funk(*args, **kwargs)
        return wrapper
    return inner


@logger(func_first=True)
def print_arg(arg):
    print(arg)


@logger()
def concat(*args, **kwargs):
    a = "".join(map(str, args)) 
    b = "".join(map(str, kwargs.values())) 
    return a + b


def randomWord(l):
    if not l:
        yield
    random.shuffle(l)
    for i in l:
        yield i
    yield from randomWord(l)


def create_account(user_name: str, password: str, secret_words: list):
    reg_password = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{6,}$")
    if not re.search(reg_password, password):
        raise ValueError("")

    def check(password_check, secret_words_check):
        if not password_check == password:
            return False
        elif len(secret_words_check) != len(secret_words):
            return False
        else:
            c1 = Counter(secret_words)
            c2 = Counter(secret_words_check)
            return len(list((c1-c2).elements())) < 2
    return check
