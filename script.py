# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(
            f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}"
        )

    def special_ability(self, turn):
        print(f"{self.name} has activated {self.special_ability}")

    def check_special_ability(self, turn):
        pass


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.special_ability_active = None
        self.special_ability_turn = None

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
        if self.special_ability_active is None:
            self.attack_power += 20
            self.special_ability_active = "Rage"
            self.special_ability_turn = turn
            print(
                f"{self.name} is raging! Attack power increased to {self.attack_power}."
            )
        else:
            print("Rage is already active!")

    def defence(self, turn):
        if self.special_ability_active is None:
            self.special_ability_active = "Defence"
            self.special_ability_turn = turn
            print(f"{self.name} is defending! Immune to attacks.")

    def check_special_ability(self, turn):

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


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)


# Mage class (inherits from Character)
class Bard(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)


# Mage class (inherits from Character)
class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == "1":
        return Warrior(name)
    elif class_choice == "2":
        return Mage(name)
    elif class_choice == "3":
        return Bard(name)
    elif class_choice == "4":
        return Cleric(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


def battle(player, wizard):
    turn = 1

    while wizard.health > 0 and player.health > 0:

        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        print(f"Active special ability: {player.special_ability_active}")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(wizard)
        elif choice == "2":
            player.special_ability(turn)
        elif choice == "3":
            pass  # Implement heal method
        elif choice == "4":
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        player.check_special_ability(turn)
        print(player.special_ability_active)
        print(player.special_ability_turn)

        turn += 1

        if wizard.health > 0:
            wizard.regenerate()
            if player.special_ability_active == "Defence":
                continue
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

        print(turn)

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
