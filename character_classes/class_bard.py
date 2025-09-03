from character import Character


# Mage class (inherits from Character)
class Bard(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=10)

        # Ability configuration
        self.abilities = {
            "1": {
                "name": "Confusion",
                "cooldown": 8,
                "duration": 4,  # Active buff duration
                "apply": self._apply_confusion,
                "remove": self._remove_confusion,
                "post_effect": None,
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

    # --- Confusion ---
    def _apply_confusion(self, wizard):
        print(
            f"{self.name} has confused {wizard.name}. Enemy attacks will apply to themselves!"
        )

    def _remove_confusion(self, wizard):
        print(f"The {wizard.name} confusion has ended")

    # --- Defence ---
    def _apply_defence(self, wizard):
        print(f"{self.name} is defending! Immune to attacks.")

    def _remove_defence(self, wizard):
        print(f"{self.name}'s defence has ended.")
