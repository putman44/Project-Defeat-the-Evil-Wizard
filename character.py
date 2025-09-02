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

    # --- Ability activation ---

    def special_ability(self, turn):
        print("\nWhich special ability would you like to use?")
        for key, ability in self.abilities.items():
            print(f"{key}. {ability['name']}")

        choice = input("Choose special ability: ")

        if choice in self.abilities:
            self._activate_ability(self.abilities[choice], turn)
        else:
            print("Invalid choice")

    def _activate_ability(self, ability, turn):
        if self.special_ability_active is None and self.special_ability_cooldown == 0:
            self.special_ability_active = ability
            self.special_ability_turn = turn
            self.special_ability_cooldown = ability["cooldown"]
            ability["apply"]()
        else:
            print("Special ability already active or on cooldown!")

    # --- Ability state management ---
    def check_special_ability(self, turn):
        # Cooldown ticking
        if self.special_ability_cooldown > 0:
            self.special_ability_cooldown -= 1

        # Handle active ability expiring
        if self.special_ability_active:
            ability = self.special_ability_active
            if turn >= self.special_ability_turn + ability["duration"]:
                ability["remove"]()
                # If ability has a post-effect, activate it
                if ability["post_effect"]:
                    self.post_effect_active = ability["post_effect"]
                    self.post_effect_turn = turn
                    self.post_effect_active["apply"]()
                # Reset active ability
                self.special_ability_active = None

        # Handle post-effect expiring
        if self.post_effect_active:
            if turn >= self.post_effect_turn + self.post_effect_active["duration"]:
                self.post_effect_active["remove"]()
                self.post_effect_active = None
                self.post_effect_turn = None
