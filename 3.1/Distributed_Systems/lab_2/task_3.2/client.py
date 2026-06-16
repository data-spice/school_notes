import Pyro4

calc = Pyro4.Proxy("PYRONAME:service.calculator")

try:
    calc.non_existent_method()
except Exception as e:
    print("Method Error:", e)
