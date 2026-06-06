# მომხმარებელს შემოატანინეთ ელფოსტის მისამართი და გადაამოწმეთ შეიცავს თუ არა '@' სიმბოლოს, შედეგი კი დაბეჭდეთ დიდი ასოებით.
Email = input("Enter your email:")
if Email.find("@") != -1:
    print("Email contains '@' symbol".upper())
else: 
    print("Email does not contain '@' symbol".upper())