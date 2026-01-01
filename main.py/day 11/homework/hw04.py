#მოსწავლეს შეეკითხეთ მის მიერ მიღებული ქულა,თუ ქულა უდრის 100-ს მაშინ გამოუტანეთ "A Group),
#თუ იქნება 80-დან 99-მდე მაშინ გამოიტანეთ "B Group",თუ იქნება 40-დან 70-მდე მაშინ "C Group",დანარჩენ შემთხვევაში კი "D Group"
score = int(input("Please enter your score: "))
if score == 100:
    print("A Group")
elif score >= 80 and score <= 99:
    print("B Group")
elif score >= 40 and score <= 70:
    print("C Group")
else:
    print("D Group")