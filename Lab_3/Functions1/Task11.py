def is_palindrome(text):
    text = ''.join(text.lower().split())
    return text == text[::-1]

word_or_phrase = input()
if is_palindrome(word_or_phrase):
    print("palindrome.")
else:
    print("not palindrome.")