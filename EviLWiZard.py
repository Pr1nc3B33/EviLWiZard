import random


# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.evading = False
        self.shielded = False

    def attack(self, opponent):
        """Deal random damage, but respect opponent's evade or shield."""
        if opponent.evading:
            print(f"{opponent.name} evades the attack!")
            opponent.evading = False
            return
        if opponent.shielded:
            print(f"{opponent.name}'s shield blocks the attack!")
            opponent.shielded = False
            return
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0

    def heal(self):
        """Restore 30 HP without exceeding max health."""
        heal_amount = 30
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} HP! Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# Warrior class — Power Strike and Shield Up
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_strike(self, opponent):
        """Deal double damage."""
        if opponent.evading:
            print(f"{opponent.name} evades the attack!")
            opponent.evading = False
            return
        if opponent.shielded:
            print(f"{opponent.name}'s shield blocks the attack!")
            opponent.shielded = False
            return
        damage = random.randint(self.attack_power - 5, self.attack_power + 5) * 2
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} uses Power Strike on {opponent.name} for {damage} damage!")

    def shield_up(self):
        """Block the next incoming attack."""
        self.shielded = True
        print(f"{self.name} raises their shield! The next attack will be blocked.")


# Mage class — Fireball and Blink
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def fireball(self, opponent):
        """Deal double damage."""
        if opponent.evading:
            print(f"{opponent.name} evades the attack!")
            opponent.evading = False
            return
        if opponent.shielded:
            print(f"{opponent.name}'s shield blocks the attack!")
            opponent.shielded = False
            return
        damage = random.randint(self.attack_power - 5, self.attack_power + 5) * 2
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} casts Fireball on {opponent.name} for {damage} damage!")

    def blink(self):
        """Evade the next incoming attack."""
        self.evading = True
        print(f"{self.name} blinks away! The next attack will be evaded.")


# Archer class — Quick Shot and Evade
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)

    def quick_shot(self, opponent):
        """Fire two arrows for double attack damage."""
        if opponent.evading:
            print(f"{opponent.name} evades the attack!")
            opponent.evading = False
            return
        if opponent.shielded:
            print(f"{opponent.name}'s shield blocks the attack!")
            opponent.shielded = False
            return
        damage = random.randint(self.attack_power - 5, self.attack_power + 5) * 2
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")

    def evade(self):
        """Evade the next incoming attack."""
        self.evading = True
        print(f"{self.name} prepares to evade the next attack!")


# Paladin class — Holy Strike and Divine Shield
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=170, attack_power=20)

    def holy_strike(self, opponent):
        """Deal attack damage plus a 15-point holy bonus."""
        if opponent.evading:
            print(f"{opponent.name} evades the attack!")
            opponent.evading = False
            return
        if opponent.shielded:
            print(f"{opponent.name}'s shield blocks the attack!")
            opponent.shielded = False
            return
        damage = random.randint(self.attack_power - 5, self.attack_power + 5) + 15
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")

    def divine_shield(self):
        """Block the next incoming attack."""
        self.shielded = True
        print(f"{self.name} activates Divine Shield! The next attack will be blocked.")
#Create additional character classes with more complex mechanics.

class Gargoyle(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=10)

    def stone_skin(self):
        """Reduce incoming damage by half for the next 3 turns."""
        self.shielded = True
        print(f"{self.name} activates Stone Skin! Incoming damage will be reduced by half for the next 3 turns.")
        
class ShapeShifter(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)

    def shapeshift(self):
        """Randomly change form to gain different stats for the next 3 turns."""
        forms = [
            {"name": "Beast Form", "health": 150, "attack_power": 25},
            {"name": "Shadow Form", "health": 100, "attack_power": 30},
            {"name": "Elemental Form", "health": 120, "attack_power": 20}
        ]
        form = random.choice(forms)
        self.health = form["health"]
        self.attack_power = form["attack_power"]
        print(f"{self.name} shapeshifts into {form['name']}! Health: {self.health}, Attack Power: {self.attack_power}")
        
                 
    
# EvilWizard class

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        """Regenerate 5 HP per turn, capped at max health."""
        regen = 5
        self.health = min(self.health + regen, self.max_health)
        print(f"{self.name} regenerates {regen} health! Current health: {self.health}/{self.max_health}")


# Special ability summon minions
    def summon_minions(self):
        """Summon minions that deal random damage to the player."""
        minion_count = random.randint(1, 3)
        print(f"{self.name} summons {minion_count} minion(s) to attack you!")
        for i in range(minion_count):
            damage = random.randint(5, 15)
            print(f"Minion {i + 1} attacks for {damage} damage!")
            self.attack_power += damage  # Minions add to the wizard's attack power for the next turn


def use_special_ability(player, wizard):
    if isinstance(player, Warrior):
        print("  1. Power Strike (double damage)")
        print("  2. Shield Up (block next attack)")
        choice = input("Choose an ability: ")
        if choice == '1':
            player.power_strike(wizard)
        elif choice == '2':
            player.shield_up()
        else:
            print("Invalid ability choice.")

    elif isinstance(player, Mage):
        print("  1. Fireball (double damage)")
        print("  2. Blink (evade next attack)")
        choice = input("Choose an ability: ")
        if choice == '1':
            player.fireball(wizard)
        elif choice == '2':
            player.blink()
        else:
            print("Invalid ability choice.")

    elif isinstance(player, Archer):
        print("  1. Quick Shot (double arrow attack)")
        print("  2. Evade (evade the next attack)")
        choice = input("Choose an ability: ")
        if choice == '1':
            player.quick_shot(wizard)
        elif choice == '2':
            player.evade()
        else:
            print("Invalid ability choice.")

    elif isinstance(player, Paladin):
        print("  1. Holy Strike (bonus damage)")
        print("  2. Divine Shield (block next attack)")
        choice = input("Choose an ability: ")
        if choice == '1':
            player.holy_strike(wizard)
        elif choice == '2':
            player.divine_shield()
        else:
            print("Invalid ability choice.")


# Character creation
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Turn-based battle loop
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            use_special_ability(player, wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            continue  # Don't consume wizard's turn when just viewing stats
        else:
            print("Invalid choice. Try again.")
            continue  # Don't consume wizard's turn on invalid input

        # Wizard's turn: regenerate then attack
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

    # End of battle — display result
    if wizard.health <= 0:
        print(f"\n*** Victory! {player.name} has defeated {wizard.name}! The kingdom is saved! ***")
    else:
        print(f"\n*** Defeat! {wizard.name} has defeated {player.name}! Darkness falls over the land... ***")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()