
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def move(self):
        print(f"{self.name} is moving.")

    def attack(self, target):
        print(f"{self.name} is attacking {target.name}.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage.")

class Player(Character):
    def __init__(self, name, health, experience):
        super().__init__(name, health)
        self.experience = experience

    def use_item(self, item):
        print(f"{self.name} is using {item}.")

    def cast_spell(self, spell):
        print(f"{self.name} is casting {spell}.")

class NPC(Character):
    def __init__(self, name, health, dialogue):
        super().__init__(name, health)
        self.dialogue = dialogue

    def talk(self):
        print(f"{self.name} says: {self.dialogue}.")

    def trade(self, item):
        print(f"{self.name} is trading {item}.")

class Monster(Character):
    def __init__(self, name, health, ability):
        super().__init__(name, health)
        self.ability = ability

    def use_ability(self):
        print(f"{self.name} uses {self.ability} ability.")