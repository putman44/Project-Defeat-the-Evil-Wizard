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

    def heal(self):
        self.health += 10
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def display_stats(self):
        print(
            f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}"
        )

    def special_ability(self, turn):
        print(f"{self.name} has activated {self.special_ability}")

    def check_special_ability(self, turn):
        pass
