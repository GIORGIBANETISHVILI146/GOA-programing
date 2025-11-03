#მომხარებელს შემოატანინე სახელი(სტრინგი), ასაკი(ინტეჯერი), და დაბადების წელი (ინტეჯერი), შემდეგ დაპრინტეთ წინადადება

#"სალამი {name}, შენ ხარ {age} წლის და დაიბადე {year} წელში
user_name = str(input("Enter your name"))
user_age = int(input("Enter your age"))
user_year = int(input("Enter your birth year"))
print("Hello" + user_name, "you are" + str(user_age) + "old", "and you birth" + str(user_year) + "year")