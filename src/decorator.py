class Drink:
    description = "Unknown drink"

    def retrieve_description(self) -> str:
        return self.description

    def cost(self) -> float:
        pass


class Espresso(Drink):

    def __init__(self):
        self.description = "Espresso Coffee"

    def cost(self) -> float:
        return 1.99


class Special(Drink):

    def __init__(self):
        self.description = "Special Coffee"

    def cost(self) -> float:
        return 0.89


class HeavilyRoasted(Drink):

    def __init__(self):
        self.description = "Heavily Roasted Coffee"

    def cost(self) -> float:
        return 0.99


class Decaffeinated(Drink):

    def __init__(self):
        self.description = "Decaffeinated Coffee"

    def cost(self) -> float:
        return 1.05


class IngredientDecorator(Drink):
    _drink: Drink = None

    def __init__(self, drink: Drink) -> None:
        self._drink = drink

    def retrieve_description(self) -> str:
        pass


class Milk(IngredientDecorator):

    def retrieve_description(self) -> str:
        return self._drink.retrieve_description() + ", Milk"

    def cost(self):
        return self._drink.cost() + 0.1


class Chocolate(IngredientDecorator):

    def retrieve_description(self) -> str:
        return self._drink.retrieve_description() + ", Chocolate"

    def cost(self):
        return self._drink.cost() + 0.2


class WhippedCream(IngredientDecorator):

    def retrieve_description(self) -> str:
        return self._drink.retrieve_description() + ", Whipped Cream"

    def cost(self):
        return self._drink.cost() + 0.1


class SoyMilk(IngredientDecorator):

    def retrieve_description(self) -> str:
        return self._drink.retrieve_description() + ", Soy Milk"

    def cost(self):
        return self._drink.cost() + 0.15



def client_code(drink: Drink):
    print(f"{drink.retrieve_description()}\nCost: {drink.cost()}")


if __name__ == "__main__":

    special = Special()
    print("I've got a special coffee!")
    client_code(special)

    print("\n")

    milk = Milk(special)
    whippedCream = WhippedCream(milk)
    print("Now I've got a decorated coffee!")
    client_code(whippedCream)
