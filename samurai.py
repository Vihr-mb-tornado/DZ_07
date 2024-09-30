from character import Character
class Samurai(Character):
    counter_damage = 0 # лічник додатковой шкоди
    max_num_damage = 5 # максимальне значення лічильника
    add_damage = 0     # додаткова шкода

    def __init__(self, name, health, damage, defence):
        Character.__init__(self, name, health, damage, defence)
        self.name = self.name + '.Samurai'  # змінюємо ім'я

    def __str__(self):
        return Character.__str__(self) + \
        f' Додаткова шкода: {self.add_damage}\n'

    def count_additional_damage(self):
        self.counter_damage = self.counter_damage + 1
        if self.counter_damage > self.max_num_damage :
            self.counter_damage = 0
        self.add_damage = self.damage * 0.1 * self.counter_damage
        return self.add_damage

    def attack(self, target):
        return target.take_damage(
            self.damage + self.count_damage_offset() + self.count_additional_damage()
        )

'''
2. Samurai - кожен удар додає 10% до базової шкоди; сумується до 5 разів (максимальний множник +50%), після чого множник обнулюється;

'''