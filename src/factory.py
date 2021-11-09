from __future__ import annotations
from abc import ABC, abstractmethod


class Pizza(ABC):

    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.clams = None
        self.pepperoni = None
        self.ingredients = []

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Baking for 25 minutes at 350 degrees")

    def cut(self):
        print("Cutting the pizza into 8 slices")

    def box(self):
        print("Placing pizza in official store box")

    def get_name(self):
        return self.name

    def get_ingredients(self):
        for key, value in self.__dict__.items():
            if key not in ['name', 'ingredient_factory', 'ingredients'] and not key.startswith('_') and value is not None:
                self.ingredients.append(str(value))
        return self.ingredients


class CheesePizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}..")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}..")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clams = self.ingredient_factory.create_clams()


class PepperoniPizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}..")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class PizzaStore(ABC):

    @abstractmethod
    def create_pizza(self, kind):
        pass

    def order_pizza(self, kind) -> Pizza:
        pizza = self.create_pizza(kind)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class ItalianPizzaStore(PizzaStore):

    def create_pizza(self, kind):
        pizza = None
        ingredient_factory = ItalianIngredientFactory()

        match kind:
            case "cheese":
                pizza = CheesePizza(ingredient_factory)
                pizza.name = "Italian Style Cheese Pizza"
            case "pepperoni":
                pizza = PepperoniPizza(ingredient_factory)
                pizza.name = "Italian Style Pepperoni Pizza"
            case "clam":
                pizza = ClamPizza(ingredient_factory)
                pizza.name = "Italian Style Clam Pizza"

        return pizza


class AmericanPizzaStore(PizzaStore):

    def create_pizza(self, kind):
        pizza = None
        ingredient_factory = AmericanIngredientFactory()

        match kind:
            case "cheese":
                pizza = CheesePizza(ingredient_factory)
                pizza.name = "American Style Cheese Pizza"
            case "pepperoni":
                pizza = PepperoniPizza(ingredient_factory)
                pizza.name = "American Style Pepperoni Pizza"
            case "clam":
                pizza = ClamPizza(ingredient_factory)
                pizza.name = "American Style Clam Pizza"

        return pizza


class PizzaIngredientFactory(ABC):

    @abstractmethod
    def create_dough(self) -> None:
        pass

    @abstractmethod
    def create_sauce(self) -> None:
        pass

    @abstractmethod
    def create_cheese(self) -> None:
        pass

    @abstractmethod
    def create_pepperoni(self) -> None:
        pass

    @abstractmethod
    def create_clams(self) -> None:
        pass


class ItalianIngredientFactory(PizzaIngredientFactory):

    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Souce:
        return MarinaraSouce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clams(self) -> Clams:
        return FreshClams()


class AmericanIngredientFactory(PizzaIngredientFactory):

    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_sauce(self) -> Souce:
        return TomatoSouce()

    def create_cheese(self) -> Cheese:
        return MozarellaCheese()

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clams(self) -> Clams:
        return FrozenClams()


class Dough:
    pass


class ThinCrustDough(Dough):
    def __str__(self):
        return "Thin Crust Dough"


class ThickCrustDough(Dough):
    def __str__(self):
        return "Thick Crust Dough"


class Souce:
    pass


class MarinaraSouce(Souce):
    def __str__(self):
        return "Marinara Souce"


class TomatoSouce(Souce):
    def __str__(self):
        return "Tomato Souce"


class Cheese:
    pass


class ReggianoCheese(Cheese):
    def __str__(self):
        return "Reggiano Cheese"


class MozarellaCheese(Cheese):
    def __str__(self):
        return "Mozarella Cheese"


class Pepperoni:
    pass


class SlicedPepperoni(Pepperoni):
    def __str__(self):
        return "Sliced Pepperoni"


class Clams:
    pass


class FrozenClams(Clams):
    def __str__(self):
        return "Frozen Clams"


class FreshClams(Clams):
    def __str__(self):
        return "Fresh Clams"


if __name__ == "__main__":

    italian_pizza_store = ItalianPizzaStore()
    american_pizza_store = AmericanPizzaStore()

    pizza = italian_pizza_store.order_pizza("cheese")
    print(f"Ethan ordered an {pizza.get_name()}")
    print(f"Ingredients: {pizza.get_ingredients()}\n")

    pizza = american_pizza_store.order_pizza("clam")
    print(f"Joel ordered a {pizza.get_name()}\n")
    print(f"Ingredients: {pizza.get_ingredients()}\n")
