from src.models.dish import Dish
import pytest


def test_dish():
    dish_spaghetti = Dish("spaghetti", 1)
    dish_bacon = Dish("bacon", 2)

    assert dish_spaghetti.name == "spaghetti"
    assert hash(dish_spaghetti) != hash(dish_bacon)
    assert hash(dish_spaghetti) == hash(dish_spaghetti)
    assert dish_spaghetti != dish_bacon
    assert dish_spaghetti == dish_spaghetti
    assert repr(dish_spaghetti) == "Dish('spaghetti', R$1.00)"

    with pytest.raises(TypeError):
        Dish("spaghetti", "spaghetti")

    with pytest.raises(ValueError):
        Dish("spaghetti", -7.00)

    dish_spaghetti.add_ingredient_dependency("cheese", 1)
    assert dish_spaghetti.recipe.get("cheese") == 1
    assert dish_bacon.get_restrictions() == set()
    assert dish_bacon.get_ingredients() == set()
