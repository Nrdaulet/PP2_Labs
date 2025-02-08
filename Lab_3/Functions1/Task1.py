def converter(grams):
    return grams / 28.3495231

grams = float(input())
ounces = converter(grams)
print(f"{grams} grams is {ounces:.2f} ounces.")