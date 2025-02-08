def unique_elements(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
result = unique_elements(input_list)
print("Unique elements:", result)