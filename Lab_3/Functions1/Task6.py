def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

user_input = input()
result = reverse_words(user_input)
print(result)