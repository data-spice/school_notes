import Pyro4

greeting = Pyro4.Proxy("PYRONAME:service.greeting")
calculator = Pyro4.Proxy("PYRONAME:service.calculator")
student = Pyro4.Proxy("PYRONAME:service.student")

print(greeting.greet())
print("15 + 10 =", calculator.add(15, 10))

data = student.getStudent()
print("Student Name:", data["name"])

