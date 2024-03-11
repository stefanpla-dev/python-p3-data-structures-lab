spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    greater_than_five = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            greater_than_five.append(food)
    return greater_than_five


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        peppers = food['heat_level'] * "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    greater_than_five = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            greater_than_five.append(food)
    
    for food in greater_than_five:
        peppers = food['heat_level'] * "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")


def get_average_heat_level(spicy_foods):
    heat_level_sum = 0
    for food in spicy_foods:
        heat_level_sum += food['heat_level']
    
    return heat_level_sum / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
