def sphere_volume(r):
    return (4 / 3) * 3.14 * (r ** 3)

r = float(input())
volume = sphere_volume(r)
print(volume)