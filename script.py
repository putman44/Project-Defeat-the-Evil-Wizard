from character import Character
from character_classes.class_warrior_chat import Warrior


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
        if player.special_ability_cooldown > 0:
            print(
                f"\nCannot use another special ability for {player.special_ability_cooldown} turns."
            )

            print(
                f"Active special ability: {player.special_ability_active['name'] if player.special_ability_active else None}\n"
            )
        else:
            print("1. Use Special Ability")
        print("2. Attack")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == "2":
            player.attack(wizard)
        elif choice == "1":
            player.special_ability(turn)
        elif choice == "3":
            player.heal()
        elif choice == "4":
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        player.check_special_ability(turn)

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
        print(f"{wizard.name} has been defeated by {player.name}!")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
