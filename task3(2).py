a = int(input("Введіть число:"))
def divide_until_less_than_50(num):
    iterations = 0
    while num >= 50:
        num /= 2
        iterations += 1
    if iterations == 0:
        print("Ви ввели надто маленьке число")
    else:
        print(f"Число, що вийшло: {num}")
        print(f"Кількість ітерацій: {iterations}")
divide_until_less_than_50(a)


