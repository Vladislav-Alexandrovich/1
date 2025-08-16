def is_year_leap(number):
    return "true" if number % 4 == 0 else "false"


number = int(input("Введите год: "))


result = is_year_leap(number)


print(f"год {number}: - {result}")
