#მომხარებელს შემოატანინე რიცხვი, და თუ ეს რიცხვი  მეტია 15 ზე, 1 დან ამ რიცხვამდე ყველა რიცხვი დაპრინტეთ  ფორ ლუპით
number = int(input("Please enter a number: "))
if number > 15:
    for i in range(1,15):
        print(i)