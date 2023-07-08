import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = list(csv_reader)
            dish_dict = dict()

            for element in rows:
                dish_name = element["dish"]
                if dish_name in dish_dict:
                    dish_dict[dish_name].append(element)
                else:
                    dish_dict[dish_name] = [element]

            for key, value in dish_dict.items():
                dish = Dish(key, float(value[0]["price"]))
                for item in value:
                    ingredient = Ingredient(item["ingredient"])
                    dish.add_ingredient_dependency(
                        ingredient, int(item["recipe_amount"])
                    )
                self.dishes.add(dish)
