import Pyro4

calc = Pyro4.Proxy("PYRONAME:service.calculator")

try:
    print(calc.divide(10, 0))
except Exception as e:
    print("Error:", e)
