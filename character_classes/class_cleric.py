from character import Character


# Mage class (inherits from Character)
class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)

        # Ability configuration
        self.abilities = {
            "1": {
                "name": "Holy Healing",
                "cooldown": 8,
                "duration": 3,  # Active buff duration
                "apply": self._apply_holy_healing,
                "remove": self._remove_holy_healing,
                "post_effect": {
                    "name": "Holy Healing",
                    "duration": 2,  # Penalty duration
                    "apply": self._apply_holy_healing_penalty,
                    "remove": self._remove_holy_healing_penalty,
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

    def heal(self):
        self.health += 30
        print(f"{self.name} regenerates 30 health! Current health: {self.health}")

    # --- Holy Healing ---
    def _apply_holy_healing(self, wizard):
        self.health += 10
        print(
            f"{self.name} has applied Holy Healing. 10+ health per turn and -10 health per turn for {wizard.name}."
        )

    def _remove_holy_healing(self, wizard):
        print(f"{self.name}'s Holy Healing has ended.")

    def _apply_holy_healing_penalty(self, wizard):
        print(
            f"{self.name}'s Holy healing prevents healing for {self.special_ability_cooldown} turns"
        )

    def _remove_holy_healing_penalty(self, wizard):
        print(
            f"{self.name} has recovered from Holy Healing effects. Able to heal again."
        )

    # --- Defence ---
    def _apply_defence(self, wizard):
        print(f"{self.name} is defending! Immune to attacks.")

    def _remove_defence(self, wizard):
        print(f"{self.name}'s defence has ended.")
