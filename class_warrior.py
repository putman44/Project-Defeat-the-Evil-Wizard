from character import Character


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.special_ability_active = None
        self.special_ability_turn = None
        self.special_ability_cooldown = 0

    def special_ability(self, turn):
        print("\nWhich special ability would you like to use?")
        print("1. Rage")
        print("2. Defence")

        choice = input("Choose special ability: ")
        if choice == "1":
            self.rage(turn)
        elif choice == "2":
            self.defence(turn)
        else:
            print("Invalid choice")

    def rage(self, turn):
        if self.special_ability_active is None and self.special_ability_cooldown == 0:
            self.attack_power += 20
            self.special_ability_active = "Rage"
            self.special_ability_turn = turn
            self.special_ability_cooldown = 8
            print(
                f"{self.name} is raging! Attack power increased to {self.attack_power}."
            )

        else:
            print("Rage is already active!")

    def defence(self, turn):
        if self.special_ability_active is None and self.special_ability_cooldown == 0:
            self.special_ability_active = "Defence"
            self.special_ability_turn = turn
            self.special_ability_cooldown = 6
            print(f"{self.name} is defending! Immune to attacks.")

    def check_special_ability(self, turn):
        if self.special_ability_cooldown > 0:
            self.special_ability_cooldown -= 1

        if (
            self.special_ability_active == "Rage"
            and turn >= self.special_ability_turn + 2
        ):
            self.attack_power -= 20
            self.special_ability_active = None
            self.special_ability_end_turn = turn

            print(
                f"{self.name}'s rage has ended. Attack power back to {self.attack_power}."
            )
        elif (
            self.special_ability_active == "Defence"
            and turn >= self.special_ability_turn + 3
        ):
            self.special_ability_active = None
            self.special_ability_end_turn = turn
            print(f"{self.name}'s defence has ended.")
