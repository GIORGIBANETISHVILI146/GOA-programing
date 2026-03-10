# შექმენით ფუნქცია Average,რომელსაც გადაცემთ 3 რიცხვს.შემდეგ კი გამოითვლით საშუალო არითმეტიკულს,საბოლოო პასუხს კი დაუმატებ 5-იანდ
def average(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    result = avg + 5
    print(result)
average(10, 20, 30)