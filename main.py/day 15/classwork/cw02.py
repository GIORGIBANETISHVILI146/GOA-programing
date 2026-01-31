# იგივე რაც ზემოთა მაგრამ პიქირით,
#  სიაში ამოჭერით ელემენტი მომხარებლის მეორე შემოტანილი რიცხვის ინდექსიდან მომხარებლის პირველი
#  შემოტანილი რიცხვის ინდექსამდე

# მაგ:  input1: 6
#      input2: 3
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# output: 4, 5, 6
input1 = int(input("Enter the first number (0-9): "))
input2 = int(input("Enter the second number (0-9): "))
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sliced_arr = arr[input2:input1]
print(sliced_arr)