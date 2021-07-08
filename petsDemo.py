class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):

        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        # self.pet = Pet(name=pet.name, type=pet.type, tricks=pet.tricks, health=pet.health, energy=pet.energy, sound=pet.sound)
        self.pet = pet




    # implement the following methods:
    def ninja_info(self):
        print("Hi my name is ", self.first_name, " and I have a lot of ", self.treats)
        print("I recently purchased " ,self.pet.name, "for $1500. But it was totally worth it because ", self.pet.name, "can ", self.pet.tricks)

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print("This is the walk method from the ninja class :-)")
        self.pet.play()
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print("I am about to give ", self.pet.name, "some", self.pet_food)
        self.pet.eat()
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print("Hey", self.pet.name, "it's time for a bathe!!")
        # print("Hey )
        self.pet.noise()

    def intro_pet(self):
        self.pet.pet_info()

class Pet:

# implement __init__( name , type , tricks, health, energy, sound ):
    # Class Attributes - to go with Class Methods
    petCounter = 0

    def __init__(self, name, type, tricks, health, sound, energy = 50):
        # Object Attributes - to go with object Methods
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound
# implement the following methods:

# Method that displayed all pet info
    def pet_info(self):
        print(self.name, self.energy, self.health, self.sound)
# sleep() - increases the pets energy by 25
    def sleep(self):
        print(self.name, "'s original energy: ",self.energy)
        self.energy += 25
        print(self.name, "'s energy after sleeping ", self.energy)
    
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        # print(self.name, "'s energy and health before eating ", self.energy, self.health)
        self.energy += 5
        self.health += 10
        # print(self.name, "'s energy and health after eating ", self.energy, self.health)
        print("Thank you for the yummy food. Watch me ", self.tricks)

# play() - increases the pet's health by 5
    def play(self):
        print("We just entered the play method in our Pet class.", self.health)
        self.health += 5
        print(self.health)
# noise() - prints out the pet's sound
    def noise(self):
        print("I am ", self.name, "hear me ",self.sound)


print("******************************")
chih = Pet("Chichi", "dog-kinda", "bark-a-lot", 0, "Yip-Yip-Yip", 500 )

bob = Pet("Bobert", "cat-cow", "flying cheese", 241, 150)

kaysee = Ninja("Kaysee", "Webers", "Dog Bones", "Purina", chih)

# chih.noise()
# bob.noise()

# kaysee.ninja_info()
# print("******************************")
# print("******************************")
# kaysee.walk()
# print("******************************")
# print("******************************")
# kaysee.feed()
# print("******************************")
# print("******************************")
# kaysee.bathe()

print(kaysee.pet.name, kaysee.pet.sound)

chih.pet_info()

kaysee.intro_pet()

# chih.sleep()
# chih.eat()
# chih.noise()