s1 = input("First word: ")
s2 = input("Second word: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagram")
else:
    print("Not Anagram")