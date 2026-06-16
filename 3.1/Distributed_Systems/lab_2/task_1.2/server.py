import Pyro4

@Pyro4.expose
class Greeting:
    def say_hello(self, name):
        return f"Hello, {name}!"

# Setup the daemon and the name server
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

# Register the greeting object
uri = daemon.register(Greeting)
ns.register("example.greeting", uri)

print("Server is ready...")
daemon.requestLoop()