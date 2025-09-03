from character import Character


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)

        # Ability configuration
        self.abilities = {
            "1": {
                "name": "Fireball",
                "cooldown": 5,
                "duration": 1,  # Active buff duration
                "apply": self._apply_fireball,
                "remove": self._remove_fireball,
                "post_effect": {
                    "name": "Fireball",
                    "duration": 2,  # Penalty duration
                    "apply": self._apply_fireball_penalty,
                    "remove": self._remove_fireball_penalty,
                },
            },
            "2": {
                "name": "Protection",
                "cooldown": 6,
                "duration": 3,
                "apply": self._apply_protection,
                "remove": self._remove_protection,
                "post_effect": None,  # No penalty/recovery
            },
        }

    # --- Fireball ---
    def _apply_fireball(self, wizard):
        self.attack_power += 80
        print(f"{self.name} has cast fireball!")
        self.attack(wizard)
        self.attack_power -= 80

    def _remove_fireball(self, wizard):
        pass

    def _apply_fireball_penalty(self, wizard):
        self.health -= 10
        print(
            f"{self.name} burned from the fireball and takes 10 damage, health decreased to {self.health}"
        )

    def _remove_fireball_penalty(self, wizard):
        print(f"{self.name}'s burning has ceased.")

    # --- Protection ---
    def _apply_protection(self, wizard):
        print(f"{self.name} has cast protection! {wizard.name} has no power here!")

    def _remove_protection(self, wizard):
        print(f"{self.name}'s protection has ended.")
