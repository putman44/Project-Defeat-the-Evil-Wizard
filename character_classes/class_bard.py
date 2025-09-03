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
                "name": "Melodic Distraction",
                "cooldown": 6,
                "duration": 3,
                "apply": self._apply_melodic_distraction,
                "remove": self._remove_melodic_distraction,
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

    # --- Melodic Distraction ---
    def _apply_melodic_distraction(self, wizard):
        print(
            f"{self.name} is playing melodic distraction. {wizard.name} is mezmerized and cannot attack!"
        )

    def _remove_melodic_distraction(self, wizard):
        print(f"{self.name}'s defence has ended.")
