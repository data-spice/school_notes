import Pyro4
# Connect to the server using the URI
uri = "PYRONAME:example.greeting"
greeting = Pyro4.Proxy(uri)
# Call remote method
print(greeting.say_hello("Alice"))
