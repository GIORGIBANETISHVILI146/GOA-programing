# მომხარებელს შემოატანინე  ერთი ინტეჯერი, და შექმენით ცვლადი სადაც შეინახება სტრიინგი,
# შემდეგ 0 ინდექსიდან მომხარებლის შემოტანილი რიცხვის  ინდექსამდე გამოიტანეთ ყველა ასო
# მაგ:  input1: 6
# string = 'aleksandre'

# output:  'aleksa'
input1 = int(input("Enter a number: "))
string = 'aleksandre'
sliced_string = string[0:input1]
print(sliced_string)