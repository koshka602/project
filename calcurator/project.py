
# print("მარტივი კალკულატორი")

# num1 = float(input("შეიყვანე პირველი რიცხვი: "))
# operator = input("აირჩიე მოქმედება (+, -, *, /): ")
# num2 = float(input("შეიყვანე მეორე რიცხვი: "))

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "ნულზე გაყოფა არ შეიძლება!"
# else:
#     result = "არასწორი მოქმედება!"

# print("პასუხი:", result)



def calculator(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "ნულზე გაყოფა არ შეიძლება"
    else:
        return "არასწორი მოქმედება"

a = float(input("პირველი რიცხვი: "))
op = input("მოქმედება (+, -, *, /): ")
b = float(input("მეორე რიცხვი: "))

print("პასუხი:", calculator(a, op, b))
