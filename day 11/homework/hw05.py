#მომხმარებელს შეეკითხეთ მისი სახელი,
#თუ ამ სახელშ იქნება ხმოვნები გამოიტანეთ ეს ხმოვნები,თუ არ იქნება გამოიტანეთ "არ არის ხმოვნები"
name = input("Please enter your name: ")
vowels = "aeiouAEIOU"
found_vowels = []
for char in name:
    if char in vowels:
        found_vowels.append(char)
if found_vowels:
    print("Vowels in your name:", ', '.join(found_vowels))
else:
    print("არ არის ხმოვნები")
