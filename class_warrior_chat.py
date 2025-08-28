from character import Character


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.special_ability_active = None  # reference to active ability dict
        self.special_ability_turn = None
        self.special_ability_cooldown = 0

        self.post_effect_active = None  # reference to post-effect dict
        self.post_effect_turn = None

        # Ability configuration
        self.abilities = {
            "1": {
                "name": "Rage",
                "cooldown": 8,
                "duration": 2,  # Active buff duration
                "apply": self._apply_rage,
                "remove": self._remove_rage,
                "post_effect": {
                    "duration": 2,  # Penalty duration
                    "apply": self._apply_rage_penalty,
                    "remove": self._remove_rage_penalty,
                },
            },
            "2": {
                "name": "Defence",
                "cooldown": 6,
                "duration": 3,
                "apply": self._apply_defence,
                "remove": self._remove_defence,
                "post_effect": None,  # No penalty/recovery
            },
        }

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

    # --- Rage ---
    def _apply_rage(self):
        self.attack_power += 20
        print(f"{self.name} is raging! Attack power increased to {self.attack_power}.")

    def _remove_rage(self):
        self.attack_power -= 40
        print(
            f"{self.name}'s rage has ended! Attack power dropped to {self.attack_power}."
        )

    def _apply_rage_penalty(self):
        print(f"{self.name} is weakened after rage...")

    def _remove_rage_penalty(self):
        self.attack_power += 20
        print(
            f"{self.name} has recovered from rage penalty. Attack power back to {self.attack_power}."
        )

    # --- Defence ---
    def _apply_defence(self):
        print(f"{self.name} is defending! Immune to attacks.")

    def _remove_defence(self):
        print(f"{self.name}'s defence has ended.")
