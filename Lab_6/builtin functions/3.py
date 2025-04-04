st = input()
st2 = st.lower()
st1 = st2[::-1]
if st1 == st2:
    print("Yes, it's palindrome")
else:
    print("No, it's not palindome")