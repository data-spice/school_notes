import Pyro4

@Pyro4.expose
class GreetingService:
    def greet(self):
        return "Hello Student"

@Pyro4.expose
class CalculatorService:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

@Pyro4.expose
class StudentService:
    def getStudent(self):
        return {"name": "Alice", "course": "Distributed Systems"}

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri1 = daemon.register(GreetingService)
uri2 = daemon.register(CalculatorService)
uri3 = daemon.register(StudentService)

ns.register("service.greeting", uri1)
ns.register("service.calculator", uri2)
ns.register("service.student", uri3)

print("Services registered")
daemon.requestLoop()
