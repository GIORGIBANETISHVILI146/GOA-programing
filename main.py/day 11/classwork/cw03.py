#მომხარებელს შემოატანინე სახელი, თუ ეს სახელი უდრის aleksandre ს, 
# დაპრინტეთ "mentor" სხვა შემთხვევაში ამ ასოში თითოეული ასო ცალ ცალკე გამოიტანეთ ფორ ლუპებით
name = input("Please enter your name: ")
if name == "aleksandre":
    print("mentor")
else:
    for char in name:
        print(char)