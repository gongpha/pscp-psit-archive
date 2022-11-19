""" _ """
def main():
    """ _ """
    ingredients = (
        "Pad Thai Sauce",
        "Tofu", "Pickle Turnip", "Shrimp",
        "Bean Sprouts", "Noodle", "Chives",
        "Lime", "Egg", "Oil", "Peanuts"
    )
    ingredients_list = list(ingredients)
    tastes = ("Sweet", "Sour", "Salty")
    tastes_list = list(tastes)

    dog_not_eat = 0 # หมาไม่ daek
    taste_not_perfecc = 0

    while True:
        iii = input()
        if iii == "Cook":
            break
        if iii not in ingredients:
            dog_not_eat = 1
            break
        if iii in ingredients_list:
            ingredients_list.remove(iii)
    while True:
        iii = input()
        if iii == "End":
            break
        if iii not in tastes:
            taste_not_perfecc = 1
            break
        if iii in tastes_list:
            tastes_list.remove(iii)
    print(
        "This is not Pad Thai!!!" if dog_not_eat else
        "This is bad!" if ingredients_list else
        "Not Bad..." if taste_not_perfecc or tastes_list else "Delicious!"
    )
main()
