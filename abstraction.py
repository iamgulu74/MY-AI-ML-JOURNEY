from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def make_sound(self):
            pass

class dog(animal):
    def make_sound(self):
        return "Woof"
    
class cat(animal):
    def make_sound(self):
        return "Meow"

dog1 = dog()
cat1 = cat()
print(dog1.make_sound()) # Output: Woof
print(cat1.make_sound()) # Output: Meow