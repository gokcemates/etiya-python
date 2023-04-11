
# sınıflar - classlar-----------------------------------------

class Human:
    # built-in  # constructor  # initialize
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer: {self.name}" 
    def talk(self,sentence):
        name = "Gökçem"
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking...")

# instance - örnek

human1 = Human("Gökçem")
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)


Human("Melike").talk("Merhaba")



# modules-----------------------------------------------------

