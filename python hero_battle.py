import random

# Base Character Class
class Character:
    def __init__(self, name, health, min_attack, max_attack):
        self.name = name
        self.health = health
        self.max_health = health
        self.min_attack = min_attack
        self.max_attack = max_attack

    def attack(self, target):
        damage = random.randint(self.min_attack, self.max_attack)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def heal(self):
        heal_amount = random.randint(10, 25)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} points! Current health: {self.health}")

    def stats(self):
        print(f"{self.name} -- Health: {self.health}/{self.max_health}")

# Warrior Class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120, min_attack=15, max_attack=25)

    def power_strike(self, target):
        damage = random.randint(25, 40)
        target.health -= damage
        print(f"{self.name} uses Power Strike! Deals {damage} damage!")

    def shield_block(self):
        print(f"{self.name} raises shield and blocks the next attack!")
        return True # next attack blocked

# Mage Class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, min_attack=10, max_attack=20)

    def fireball(self, target):
        damage = random.randint(20, 35)
        target.health -= damage
        print(f"{self.name} casts Fireball! Deals {damage} damage!")

    def mana_barrier(self):
        print(f"{self.name} casts Mana Barrier and reduces incoming damage by half next turn!")
        return True # next attack reduced

# Archer Class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, min_attack=12, max_attack=22)

    def quick_shot(self, target):
        damage1 = random.randint(10, 18)
        damage2 = random.randint(10, 18)
        total = damage1 + damage2
        target.health -= total
        print(f"{self.name} uses Quick Shot! Hits twice for {damage1} + {damage2} = {total} damage!")

    def evade(self):
        print(f"{self.name} prepares to evade the next attack!")
        return True # evade next attack

# Paladin Class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=110, min_attack=13, max_attack=23)

    def holy_strike(self, target):
        damage = random.randint(22, 35)
        target.health -= damage
        print(f"{self.name} uses Holy Strike! Deals {damage} damage!")

    def divine_shield(self):
        print(f"{self.name} uses Divine Shield and blocks the next attack!")
        return True # next attack blocked

# Evil Wizard
class EvilWizard(Character):
    def __init__(self):
        super().__init__("Evil Wizard", health=150, min_attack=15, max_attack=25)

    def regenerate(self):
        regen = random.randint(10, 20)
        self.health = min(self.health + regen, self.max_health)
        print(f"Evil Wizard regenerates {regen} health! Current health: {self.health}")

# Game Loop
def battle(player, enemy):
    block_next = False # For abilities like shield or evade

    while player.health > 0 and enemy.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack\n2. Heal\n3. Use Ability\n4. View Stats")
        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(enemy)
        elif choice == "2":
            player.heal()
        elif choice == "3":
            if isinstance(player, Warrior):
                print("1. Power Strike\n2. Shield Block")
                ability = input("Choose ability: ")
                if ability == "1":
                    player.power_strike(enemy)
                else:
                    block_next = player.shield_block()
            elif isinstance(player, Mage):
                print("1. Fireball\n2. Mana Barrier")
                ability = input("Choose ability: ")
                if ability == "1":
                    player.fireball(enemy)
                else:
                    block_next = player.mana_barrier()
            elif isinstance(player, Archer):
                print("1. Quick Shot\n2. Evade")
                ability = input("Choose ability: ")
                if ability == "1":
                    player.quick_shot(enemy)
                else:
                    block_next = player.evade()
            elif isinstance(player, Paladin):
                print("1. Holy Strike\n2. Divine Shield")
                ability = input("Choose ability: ")
                if ability == "1":
                    player.holy_strike(enemy)
                else:
                    block_next = player.divine_shield()
        elif choice == "4":
            player.stats()
            enemy.stats()
            continue
        else:
            print("Invalid choice. Try again.")
            continue

        # Check if enemy defeated
        if enemy.health <= 0:
            print("\nYou have defeated the Evil Wizard! Victory is yours!")
            break

        # Enemy's turn
        print("\n--- Evil Wizard's Turn ---")
        enemy.regenerate()
        if block_next:
            print(f"{player.name} blocked or evaded the attack!")
            block_next = False
        else:
            enemy.attack(player)
            if player.health <= 0:
                print("\nThe Evil Wizard has defeated you. Game Over.")
                break

# Game Start
def start_game():
    print("Choose your hero class:")
    print("1. Warrior\n2. Mage\n3. Archer\n4. Paladin")
    choice = input("Enter choice: ")

    name = input("Enter your hero's name: ")

    if choice == "1":
        player = Warrior(name)
    elif choice == "2":
        player = Mage(name)
    elif choice == "3":
        player = Archer(name)
    elif choice == "4":
        player = Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player = Warrior(name)

    enemy = EvilWizard()
    battle(player, enemy)

# Run the game
start_game()