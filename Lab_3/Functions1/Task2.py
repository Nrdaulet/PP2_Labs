def tempconverter(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

fahrenheit = float(input())
celsius = tempconverter(fahrenheit)
print(f"{fahrenheit}°F is {celsius:.2f}°C.")