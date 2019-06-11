class Person:
    def __init__(self, name, age, pay=0, job=None): # method
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software') # class instance (addresses to atributes)
    sue = Person('Sue Jones', 45, 40000, 'hardware') # class instance
    print(bob.name, sue.pay)

    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print(sue.pay)

# about OOP https://python-scripts.com/object-oriented-programming-in-python
