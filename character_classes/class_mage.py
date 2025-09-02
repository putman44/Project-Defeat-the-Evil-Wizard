from character import Character


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)
        self.special_ability_active = None  # reference to active ability dict
        self.special_ability_turn = None
        self.special_ability_cooldown = 0

        self.post_effect_active = None  # reference to post-effect dict
        self.post_effect_turn = None

        # Ability configuration
        self.abilities = {
            "1": {
                "name": "Fireball",
                "cooldown": 5,
                "duration": 1,  # Active buff duration
                "apply": self._apply_fireball,
                "remove": self._remove_fireball,
                "post_effect": {
                    "duration": 2,  # Penalty duration
                    "apply": self._apply_fireball_penalty,
                    "remove": self._remove_fireball_penalty,
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

    # --- Rage ---
    def _apply_fireball(self, wizard):
        self.attack_power += 80
        print(f"{self.name} has cast fireball!")
        self.attack(wizard)
        self.attack_power -= 80

    def _remove_fireball(self):
        pass

    def _apply_fireball_penalty(self):
        self.health -= 10
        print(
            f"{self.name} burned from the fireball, health decreased to {self.health}"
        )

    def _remove_fireball_penalty(self):
        print(f"{self.name}'s burning has ceased.")

    # --- Defence ---
    def _apply_defence(self, wizard):
        print(f"{self.name} is defending! Immune to attacks.")

    def _remove_defence(self):
        print(f"{self.name}'s defence has ended.")
