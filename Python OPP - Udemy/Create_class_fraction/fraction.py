class Fraction:
    def __init__(self):
        self.num = 0
        self.deno = 1

    def set_input_fraction(self):
        self.num, self.deno = map(int, input().split())

    def add(self, fraction2):
        num = (self.num * fraction2.deno + fraction2.num * self.deno)
        deno = self.deno * fraction2.deno
        return num, deno

    def sub(self, fraction2):
        num = (self.num * fraction2.deno - fraction2.num * self.deno)
        deno = self.deno * fraction2.deno
        return num, deno

    def multiplication(self, fraction2):
        num = self.num * fraction2.num
        deno = self.deno * fraction2.deno
        return num, deno

    def divison(self, fraction2):
        num = self.num * fraction2.deno
        deno = self.deno * fraction2.num
        return num, deno

    def print_fraction(self, fraction2):
        print(
            f'{self.add(fraction2)[0]}/{self.add(fraction2)[1]} ')
        print(
            f'{self.sub(fraction2)[0]}/{self.sub(fraction2)[1]} ')
        print(
            f'{self.multiplication(fraction2)[0]}/{self.multiplication(fraction2)[1]} ')
        print(
            f'{self.divison(fraction2)[0]}/{self.divison(fraction2)[1]}  ')


object1 = Fraction()
object2 = Fraction()
object1.set_input_fraction()
object2.set_input_fraction()
object1.print_fraction(object2)
