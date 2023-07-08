from src.models.ingredient import Ingredient


def test_ingredient():
    pork_bacon = Ingredient("bacon")
    beef_bacon = Ingredient("bacon")
    egg = Ingredient("egg")

    assert pork_bacon.__hash__() == beef_bacon.__hash__()
    assert pork_bacon.__hash__() != egg.__hash__()
    assert pork_bacon == pork_bacon
    assert beef_bacon != egg
    assert repr(pork_bacon) == "Ingredient('bacon')"
    assert beef_bacon.name == "bacon"
    invalid_instance = Ingredient("xablau")
    assert invalid_instance.restrictions == set()
