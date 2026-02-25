# მომხმარებელს შემოატანინეთ სიტყვა და შეამოწმეთ, არის თუ არა იგი დიდი ასოებით, თუ კი — დაბეჭდე "სიტყვა უკვე დიდია!", თუ არა — გადააქციე და დაბეჭდე.
string = input("Enter your string:")
if string.isupper():
    print("string is uppercase")
else:
    print(string.upper())
    print("string is uppercase now")