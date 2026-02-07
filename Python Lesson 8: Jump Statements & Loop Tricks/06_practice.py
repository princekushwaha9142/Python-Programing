text = input("Enter a string: ")

for ch in text:
    if ch.lower() in "aeiou":
        print("First vowel found:", ch)
        break
else:
    print("No vowel found in the string")