class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(cls, s):
        firstname, lastname, salary = s.split("-")
        return cls(firstname, lastname, int(salary))


# emp2 = Employee.from_string("John-Smith-55000")
# print(type(emp2))
# print(emp2.firstname)
# print(emp2.lastname)
# print(emp2.salary)
# print(isinstance(emp2.salary, int))


class Pizza:
    order_number = 0
    ingredients = []

    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients
        Pizza.order_number += 1
        self.order_number = Pizza.order_number

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])


# p1 = Pizza(['bacon', 'parmesan', 'ham'])
# print(p1.ingredients)
# print(p1.order_number)
# p2 = Pizza.garden_feast()
# print(p2.ingredients)
# p3 = Pizza.hawaiian()
# print(p3.ingredients)
# print(p1.order_number)
# p4 = Pizza.meat_festival()
# print(p4.ingredients)
# p5 = Pizza(["pepperoni", "bacon"])
# print(p5.ingredients)
# my_pizza = Pizza(['cheese', 'caviar', 'oyster', 'uranium'])
# print(my_pizza.ingredients)
# print(p1.order_number)
# print(p2.order_number)
# print(p3.order_number)
# print(p4.order_number)
# print(p5.order_number)
# print(my_pizza.order_number)


class Employee1:
    def __init__(self, s, **kwargs) -> None:
        self.name, self.lastname = s.split(" ")
        for k, v in kwargs.items():
            setattr(Employee, k, v)

# mary = Employee('Mary Major', salary=120000)
# print(mary.salary)


class Gallows:
    def __init__(self) -> None:
        self.game_over = False
        self.words = []

    def play(self, s):
        if not self.words:
            self.words.append(s)
            return self.words

        if s in self.words:
            self.game_over = True
            return "game over"

        if self.words:
            if self.words[-1][-1] == s[0]:
                self.words.append(s)
                return self.words
            self.game_over = True
            return "game over"

    def restart(self):
        self.words.clear()
        self.game_over = False
        return "game restarted"


class Testpaper:
    def __init__(self, subject, markscheme, pass_mark) -> None:
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self) -> None:
        self._tests_taken = {}

    @property
    def tests_taken(self):
        if not self._tests_taken:
            return "No tests taken"
        return self._tests_taken

    def take_test(self, paper, answers):
        val_ans = 100 / (len(answers))
        result = 0
        for i in range(len(answers)):
            if paper.markscheme[i] == answers[i]:
                result += val_ans

        is_passing = result < int(paper.pass_mark[0:2])
        attitude = f"Failed! ({round(result)}%)" if is_passing else f"Passed! ({round(result)}%)"
        self._tests_taken[paper.subject] = attitude
        return self._tests_taken


paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
student1 = Student()
print(student1.tests_taken)
student1.take_test(paper1, ['1A', '2D', '3D', '4A', '5A'])
print(student1.tests_taken)
print(paper1.subject)
print(paper1.markscheme)
print(paper1.pass_mark)
