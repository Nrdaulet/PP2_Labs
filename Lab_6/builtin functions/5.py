def all_true(a):
    return all(a)

print(all_true((True, True, True)))
print(all_true((True, False, True)))
print(all_true((1, 4, 5, 7, 2)))
print(all_true((4, 8, 0, 5)))
print(all_true(("", 'Hello world', 'nur'))) #empty gap is false