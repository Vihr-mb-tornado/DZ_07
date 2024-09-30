from character import Character
class Berserk(Character):
    max_health = 100
    counter_life = 1

    def __init__(self, name, health, damage, defence):
        Character.__init__(self, name, health, damage, defence)

    def __str__(self):
        return Character.__str__(self) + \
        f'Додаткова шкода: {self.count_additional_damage()}'

    def count_additional_damage(self):
        return max(self.damage * (1 - self.health / self.max_health), 0)

    def attack(self, target):
        return target.take_damage(
            self.damage + self.count_damage_offset() + self.count_additional_damage()
        )

    def take_damage(self, damage):
        real_damage = Character.take_damage(self, damage)
        if self.health <= 0:
            if self.counter_life==1:
                self.counter_life=0
                self.health=1
        return real_damage

'''
Додати до класу Berserk механіку останнього шансу: якщо Berserk отримує смертельну шкоду,
його здоров'я одноразово піднімається до 1. Наступна смертельна шкода опускає здоров'я
до нуля.м
'''