class Player:
  def __init__(self, name, hit_points, attack_points, defense_points):
    self.name = name
    self.hit_points = hit_points
    self.attack_points = attack_points
    self.defense_points = defense_points
    self.equipped_weapon = None
    self.equipped_armour = None
 
  def attack(self, monster):
    damage = self.attack_points
    if self.equipped_weapon:
      damage += self.equipped_weapon.attack_points
    monster.hit_points -= damage
 
  def defend(self):
    self.defense_points += 2
 
  def equip_weapon(self, weapon):
    self.equipped_weapon = weapon
 
  def equip_armour(self, armour):
    self.equipped_armour = armour

class Monster:
  def __init__(self, name, hit_points, attack_points, defense_points):
    self.name = name
    self.hit_points = hit_points
    self.attack_points = attack_points
    self.defense_points = defense_points
 
  def attack(self, player):
    damage = self.attack_points
    if player.equipped_armour:
      damage -= player.equipped_armour.defense_points
    player.hit_points -= damage

class Weapon:
  def __init__(self, name, attack_points):
    self.name = name
    self.attack_points = attack_points

class Armour:
  def __init__(self, name, defense_points):
    self.name = name
    self.defense_points = defense_points

class Game:
  def start(self):
    # create player and monsters
    player = Player('Player', 10, 2, 0)
    monster1 = Monster('Monster 1', 5, 1, 0)
    monster2 = Monster('Monster 2', 7, 2, 0)
    monsters = [monster1, monster2]
   
    # create weapons and armour
    weapon1 = Weapon('Sword', 3)
    weapon2 = Weapon('Axe', 4)
    armour1 = Armour('Chainmail', 1)
    armour2 = Armour('Plate Armour', 2)
   
    # start game loop
    while True:
      # player turn
      print('It is your turn!')
      print('What would you like to do?')
      print('1. Attack')
      print('2. Defend')
      print('3. Equip Weapon')
      print('4. Equip Armour')
      action = input('Enter the number of your choice: ')
      print(" ")
     
      if action == '1':
        monster = self.choose_monster(monsters)
        player.attack(monster)
        print(f'You attack {monster.name} for {player.attack_points} damage!')
        if monster.hit_points <= 0:
          monsters.remove(monster)
          print(f'{monster.name} has been defeated!')
     
      elif action == '2':
        player.defend()
        print('You defend and block the attack!')
       
      elif action == '3':
        weapon = self.choose_weapon([weapon1, weapon2])
        player.equip_weapon(weapon)
        print(f'You equip the {weapon.name}')
     
      elif action == '4':
        armour = self.choose_armour([armour1, armour2])
        player.equip_armour(armour)
        print(f'You equip the {armour.name}\n')
     
      # monsters turn
      for monster in monsters:
        monster.attack(player)
        print(f'{monster.name} attacks you for {monster.attack_points} damage!')
        if player.hit_points <= 0:
          print('You have been defeated!')
          return
      print(" ")
     
      # check if all monsters have been defeated
      if not monsters:
        print('You have defeated all the monsters!')
        return
     
  def choose_monster(self, monsters):
    print('Which monster do you want to attack?')
    for i, monster in enumerate(monsters):
      print(f'{i+1}. {monster.name}')
    choice = int(input('Enter the number of your choice: '))
    return monsters[choice-1]
 
  def choose_weapon(self, weapons):
    print('Which weapon do you want to equip?')
    for i, weapon in enumerate(weapons):
      print(f'{i+1}. {weapon.name}')
    choice = int(input('Enter the number of your choice: '))
    return weapons[choice-1]
 
  def choose_armour(self, armours):
    print('Which armour do you want to equip?')
    for i, armour in enumerate(armours):
      print(f'{i+1}. {armour.name}')
    choice = int(input('Enter the number of your choice: '))
    return armours[choice-1]

game = Game()
game.start()