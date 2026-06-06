#შექმენით სია, და მომხარებელს შემოატანინეთ რიცხვი,
#შემდეგ თუ ეს რიცხვი მეტია 5 ზე, მაგ ინდექსზე მდგომი ელემენტი გამოიტანეთ
elements = ["gio", "apple", "mamaflex" , 14, 2.3, True, 3, 1.1,
 False, "kai ra", 112, "white", "blue", 20, 67, 6767, "eh", "hoo", "xoo"]
user_number = int(input("Enter your number:"))
if user_number>5:
    print(elements[user_number])
else:
    print("nothing")