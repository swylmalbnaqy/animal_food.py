# animal_food.py

def calculate_food_amount(weight, activity_level):
    if activity_level == "низкая":
        food_amount = weight * 0.02
    elif activity_level == "средняя":
        food_amount = weight * 0.03
    else:
        food_amount = weight * 0.04
    return food_amount

weight = float(input("Введите вес животного (в кг): "))
activity_level = input("Введите уровень активности животного (низкая, средняя, высокая): ")

food_amount = calculate_food_amount(weight, activity_level)

print("Ежедневное количество еды для животного: ", food_amount, "кг")
