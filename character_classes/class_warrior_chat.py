from character import Character


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=15)

        # Ability configuration
        self.abilities = {
            "1": {
                "name": "Rage",
                "cooldown": 8,
                "duration": 2,  # Active buff duration
                "apply": self._apply_rage,
                "remove": self._remove_rage,
                "post_effect": {
                    "name": "Rage",
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

    # --- Rage ---
    def _apply_rage(self, wizard):
        self.attack_power += 45
        print(f"{self.name} is raging! Attack power increased to {self.attack_power}.")

    def _remove_rage(self, wizard):
        self.attack_power -= 45

    def _apply_rage_penalty(self, wizard):
        self.attack_power -= 10
        print(
            f"{self.name} is weakened after rage, attack power decreased to {self.attack_power}"
        )

    def _remove_rage_penalty(self, wizard):
        self.attack_power += 10
        print(
            f"{self.name} has recovered from rage penalty. Attack power back to {self.attack_power}."
        )

    # --- Defence ---
    def _apply_defence(self, wizard):
        print(f"{self.name} is defending! Immune to attacks.")

    def _remove_defence(self, wizard):
        print(f"{self.name}'s defence has ended.")
