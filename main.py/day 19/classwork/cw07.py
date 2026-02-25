# მომხარებელს შემოატანინე სტრინგი. შეამოწმე — სულ პატარა ასოებით არის თუ არა. თუ არის დაპრინტე "string is lowercase", სხვა შემთხვევაში "string is uppercase"
name = input("Enter your name:")

if name.islower():
    print("string is lowercase")
else:
    print("string is uppercase")