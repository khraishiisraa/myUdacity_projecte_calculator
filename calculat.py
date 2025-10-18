
#  نستدعي مكتبه math لاستخدام امرين math.squr() ,math.pow(,)
import math   

def calculator():
    print("<< A simple Calculator with math module >>")

    #     string قراءة اول رقم و فحص انه رقم وليس 
    while True:
        first = input("Enter first number: ")
        try:
            result = float(first)
            break
        except ValueError:
            print("Invalid number. Try again.")
# ادخال العملية ضمن الخيارت ادناه مع ازالة الفراغ
    while True:
        operator = input("Enter operator (+, -, *, /, ^, sqrt, =): ").strip() 
# اذا ادخل = فان العملية تنتهي بطباعة النتيجة
        if operator == '=':
            break
#  و اذا لم تكن العملية ضمن الخيارات
        if operator not in ['+', '-', '*', '/', '^', 'sqrt']:
            print("Invalid operator. Try again.")
            continue
# لعملية الجذر نحتاج فحص العدد ليس سالب
        if operator == 'sqrt':
            if result < 0:
                print("Math ERROR: Cannot take sqrt of negative number.")
                continue
            result = math.sqrt(result)
            print(f"Current result: {result}")
            continue

 #  لبقية العمليات نحتاج رقم ثاني
        next_input = input("Enter next number: ")
        try:
            number = float(next_input)
        except ValueError:
            print("Invalid number. Try again.")
            continue

        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
        elif operator == '*':
            result *= number
            #  هنا يوجد فحص للمقام 
        elif operator == '/':
            if number == 0:
                print("Math ERROR: Cannot divide by zero.")
            else:    # continue
             result /= number
        elif operator == '^':
            result = math.pow(result, number)
# لاظهار النتيجه بعد كل عمليةكما في الالة الحاسبة البسيطة
        print(f"Current result: {result}")
# النتيجة النهاية
    print(f"The final result: {result}")

calculator()

