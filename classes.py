# -------------------------------------------------------------------------
class Car():
   def __init__(self, color, manufacturer, model = "truck", year = 2026):
       self.color = color
       self.manufacturer = manufacturer
       self.model = model
       self.year = year

mycar = Car("grey", "BMW")
print(mycar.model)
print(mycar.year)
# -------------------------------------------------------------------------
class Solid():
    pass
    
    def surfacearea(self):
        pass

    def volume(self):
        pass

class Cube(Solid):
    def __init__(self, dblsidelength):
        self.side_length = dblsidelength

    def surfacearea(self):
        surface_area = 6 * (self.side_length ** 2)

    def volume(self):
        volume = self.side_length ** 3

class Sphere(Solid):
    def __init__(self,dblradius):
        self.radius = dblradius

    def surfacearea(self):
        surface_area = 4 * 3.14 * (self.radius ** 2)

    def volume(self):
        volume = 1.333 * 3.14 * (self.radius ** 3)
# --------------------------------------------------------------------------
class Employee():
    def describe(self):
        print("I am an employee.")

class Manager(Employee):
    def describe(self):
        super().describe()
        print("I manage a team.")

mymanager = Manager()
mymanager.describe()
# ---------------------------------------------------------------------------
class Account():
    def __init__(self, accountnumber, balance):
        self.account_number = accountnumber
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, accountnumber, balance, interestrate):
        super().__init__(accountnumber, balance)
        # super().__init__(balance)
        self.interest_rate = interestrate

    def display_account(self):
        print(self.account_number)
        print(self.balance)
        print(self.interest_rate)

    def add_interest(self):
        adding_amount = self.balance * self.interest_rate
        self.balance += adding_amount
        return self.balance

mysavings = SavingsAccount(2, 500, 0.10)
mysavings.display_account()
print(mysavings.add_interest())