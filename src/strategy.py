from __future__ import annotations


class Character:

    def __init__(self, weapon_behavior: WeaponBehavior) -> None:
        self._weapon_behavior = weapon_behavior

    def fight(self):
        self._weapon_behavior.use_weapon()

    @property
    def weapon_behavior(self) -> WeaponBehavior:
        return self._weapon_behavior

    @weapon_behavior.setter
    def weapon_behavior(self, behavior: WeaponBehavior) -> None:
        self._weapon_behavior = behavior


class Queen(Character):

    def __init__(self, weapon_behavior: WeaponBehavior):
        super().__init__(weapon_behavior)


class King(Character):

    def __init__(self, weapon_behavior: WeaponBehavior):
        super().__init__(weapon_behavior)


class Knight(Character):

    def __init__(self, weapon_behavior: WeaponBehavior):
        super().__init__(weapon_behavior)


class Troll(Character):

    def __init__(self, weapon_behavior: WeaponBehavior):
        super().__init__(weapon_behavior)


class WeaponBehavior:

    def use_weapon(self):
        raise NotImplementedError


class SwordBehavior(WeaponBehavior):

    def use_weapon(self):
        print("Whing!")


class KnifeBehavior(WeaponBehavior):

    def use_weapon(self):
        print("Stab!")


class BowAndArrowsBehavior(WeaponBehavior):

    def use_weapon(self):
        print("Thwang.. Swish!")


class BattleAxBehavior(WeaponBehavior):

    def use_weapon(self):
        print("Swoosh!")


if __name__ == "__main__":

    queen = Queen(KnifeBehavior())
    queen.fight()

    king = King(SwordBehavior())
    king.fight()

    king.weapon_behavior = BowAndArrowsBehavior()
    king.fight()
